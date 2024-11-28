FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . /app

COPY .env /app/.env

# Install GTK-3 and other necessary dependencies
# RUN apt-get update && apt-get install -y \
#     libgtk-3-dev 

# COPY ./build.sh /app/build.sh
RUN chmod +x /app/build.sh
RUN chmod +x /app/.env

