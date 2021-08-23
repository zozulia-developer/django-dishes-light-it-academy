FROM python:3.8-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ['bash', '/app/docker-entrypoint.sh']