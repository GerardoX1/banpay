FROM python:3.11-slim

RUN apt-get update -y --fix-missing

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./start-web /start-web
RUN sed -i 's/\r$//g' /start-web
RUN chmod +x /start-web

WORKDIR /app
