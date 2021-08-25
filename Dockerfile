FROM python:3.8-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["bash", "/app/docker-entrypoint.sh"]