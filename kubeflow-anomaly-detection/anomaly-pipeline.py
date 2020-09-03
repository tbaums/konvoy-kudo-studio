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
def fetch_data_op(anomalous_data_path: OutputPath(str), non_anomalous_data_path: OutputPath(str)):
    import sys, subprocess;
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pandas'])

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

    print(f'Anomalous data saved to {anomalous_data_path}')
    print(f'Non-anomalous data saved to {non_anomalous_data_path}')

@func_to_container_op
def prep_data_op(anomalous_data_path: InputPath(str), non_anomalous_data_path: InputPath(str)):
    import sys, subprocess;
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pandas'])

    import os
    import pandas as pd 

    df_small_noise = pd.read_csv(non_anomalous_data_path)
    df_daily_jumpsup = pd.read_csv(anomalous_data_path)

    print(df_small_noise.head())
    print(df_daily_jumpsup.head())

    


@dsl.pipeline(
    name='Anomaly Detection', 
    description='Example anomaly detection on-airframe'
) 
def anomaly_pipeline():
    fetched_data = fetch_data_op()
    print(fetched_data.outputs)
    prepped_data = prep_data_op(fetched_data.outputs['non_anomalous_data'], fetched_data.outputs['anomalous_data'])



