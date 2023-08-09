# pull official base image
FROM python:3.9 

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY ./requirements.txt .
RUN cat requirements.txt


RUN pip install -r requirements.txt

# copy project
COPY . .
