# Borrowed from https://keras.io/examples/timeseries/timeseries_anomaly_detection/
# Expanded to include KFP by M Tanenbaum, D2iQ - Github: @tbaums

import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from typing import NamedTuple
import kfp.components as components
import kfp.dsl as dsl
import kubeflow.fairing.utils
from kfp.components import func_to_container_op, InputPath, OutputPath


@func_to_container_op
def fetch_data_op(
    anomalous_data_path: OutputPath(str),
    non_anomalous_data_path: OutputPath(str),
):
    # Need to install Pandas because base image does not include
    import sys, subprocess

    subprocess.run([sys.executable, "-m", "pip", "install", "pandas"])

    import os
    import pandas as pd

    master_url_root = "https://raw.githubusercontent.com/numenta/NAB/master/data/"

    df_small_noise_url_suffix = "artificialNoAnomaly/art_daily_small_noise.csv"
    df_small_noise_url = master_url_root + df_small_noise_url_suffix
    df_small_noise = pd.read_csv(
        df_small_noise_url, parse_dates=True, index_col="timestamp"
    )

    df_daily_jumpsup_url_suffix = "artificialWithAnomaly/art_daily_jumpsup.csv"
    df_daily_jumpsup_url = master_url_root + df_daily_jumpsup_url_suffix
    df_daily_jumpsup = pd.read_csv(
        df_daily_jumpsup_url, parse_dates=True, index_col="timestamp"
    )

    print("Non-anomalous Data")
    print(df_small_noise.describe())

    print("Anomalous Data")
    print(df_daily_jumpsup.describe())

    df_daily_jumpsup.to_csv(anomalous_data_path)
    df_small_noise.to_csv(non_anomalous_data_path)

    print(f"Anomalous data saved to {anomalous_data_path}")
    print(f"Non-anomalous data saved to {non_anomalous_data_path}")


@func_to_container_op
def prep_data_op(
    anomalous_data_path: InputPath(str),
    non_anomalous_data_path: InputPath(str),
    x_train_path: OutputPath(str),
):
    # Need to install Pandas because base image does not include
    import sys, subprocess

    subprocess.run([sys.executable, "-m", "pip", "install", "pandas"])

    import os
    import pandas as pd
    import numpy as np

    df_small_noise = pd.read_csv(non_anomalous_data_path)
    df_daily_jumpsup = pd.read_csv(anomalous_data_path)

    print("Successfully retrieved sample data. \n Beginning data prep...")
    print(df_small_noise.head())
    print(df_daily_jumpsup.head())
    print("Starting data checks...")
    try:
        print(f"df_small_noise.iloc[0].value == {df_small_noise.iloc[0].value}")
        assert df_small_noise.iloc[0].value == 19.761251902999998
        print("df_small_noise.iloc[0].value check passed!")
    except:
        sys.exit("Data validation failed for df_small_noise.iloc[0].value")
    try:
        print(f"df_daily_jumpsup.iloc[0].value == {df_daily_jumpsup.iloc[0].value}")
        assert df_daily_jumpsup.iloc[0].value == 18.324918539200002
        print("df_daily_jumpsup.iloc[0].value check passed!")
    except:
        sys.exit("Data validation failed for df_daily_jumpsup.iloc[0].value")
    print("Completed data checks. \n ...... \n Creating sequences...")

    # Normalize and save the mean and std we get,
    # for normalizing test data.
    training_mean = df_small_noise.mean()
    training_std = df_small_noise.std()
    df_training_value = (df_small_noise - training_mean) / training_std
    print("Number of training samples:", len(df_training_value))

    """
    ### Create sequences
    Create sequences combining `TIME_STEPS` contiguous data values from the
    training data.
    """

    TIME_STEPS = 288

    # Generated training sequences for use in the model.
    def create_sequences(values, time_steps=TIME_STEPS):
        output = []
        for i in range(len(values) - time_steps):
            output.append(values[i : (i + time_steps)])
        return np.stack(output)

    x_train = create_sequences(df_training_value.values)
    print("Training input shape: ", x_train.shape)
    # TODO - training input shape is (3744, 288, 2) - should be (3744, 288, 1)
    # Maybe just drop the second one? wtf is happening here?

    if not os.path.isdir(x_train_path):
        os.makedirs(x_train_path)

    np.save(f"{x_train_path}/x_train", x_train)

    print(f"Saved training data to {x_train_path}")


@func_to_container_op
def build_and_train_model_op(x_train_path: InputPath(str), model_path: OutputPath(str)):
    # Need to upgrade to TF 2.3.0 to get Conv1DTranspose in Keras (below)
    import sys, subprocess

    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "tensorflow==2.3"])
    
    import numpy as np
    from tensorflow import keras
    from tensorflow.keras import layers

    print("Loading training data...")
    x_train = np.asarray(np.load(f"{x_train_path}/x_train.npy", allow_pickle=True))
    print("Loaded training data. \n Assembling model... \n")

    """
    ## Build a model

    We will build a convolutional reconstruction autoencoder model. The model will
    take input of shape `(batch_size, sequence_length, num_features)` and return
    output of the same shape. In this case, `sequence_length` is 288 and
    `num_features` is 1.
    """

    model = keras.Sequential(
        [
            layers.Input(shape=(x_train.shape[1], x_train.shape[2])),
            layers.Conv1D(
                filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Dropout(rate=0.2),
            layers.Conv1D(
                filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Conv1DTranspose(
                filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Dropout(rate=0.2),
            layers.Conv1DTranspose(
                filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
            ),
            layers.Conv1DTranspose(filters=1, kernel_size=7, padding="same"),
        ]
    )
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss="mse")
    print(model.summary())

    print("Model compiled. \n Begin model training... \n")

    """
    ## Train the model

    Please note that we are using `x_train` as both the input and the target
    since this is a reconstruction model.
    """

    history = model.fit(
        x_train,
        x_train,
        epochs=10,
        batch_size=128,
        validation_split=0.1,
        callbacks=[
            keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, mode="min")
        ],
    )

    print(f"\n \n \n Model trained. Saving model to {model_path}")


@dsl.pipeline(
    name="Anomaly Detection", description="Example anomaly detection on-airframe"
)
def anomaly_pipeline():
    fetched_data = fetch_data_op()
    prepped_data = prep_data_op(
        fetched_data.outputs["non_anomalous_data"],
        fetched_data.outputs["anomalous_data"],
    )
    built_and_trained_model_ = build_and_train_model_op(prepped_data.outputs["x_train"])
