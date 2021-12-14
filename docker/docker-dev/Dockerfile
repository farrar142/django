FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY requirements.txt .
COPY ../../. .

RUN pip3 install -r requirements.txt \
    && apt-get update \
    && ln -s local_user/jenkins_home/build var/jenkins_home/build

ENTRYPOINT python manage.py runserver 0.0.0.0:8000

EXPOSE 8000