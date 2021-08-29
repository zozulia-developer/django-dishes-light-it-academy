FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y\
    build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt