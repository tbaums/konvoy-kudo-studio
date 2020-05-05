FROM python:3.7.3-alpine3.10
WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app/templates
RUN pip install --upgrade pip
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt
COPY prediction-api.py ./
CMD [ "python", "-u", "prediction-api.py"]
