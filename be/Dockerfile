FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt 

CMD gunicorn -b 0.0.0.0:80 main:app