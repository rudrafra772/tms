FROM python:3.12-slim

#ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . /app

# Install GTK-3 and other necessary dependencies
# RUN apt-get update && apt-get install -y \
#     libgtk-3-dev 

# COPY ./build.sh /app/build.sh
RUN chmod +x /app/build.sh

