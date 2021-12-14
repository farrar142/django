FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY requirements.txt .
COPY . .

RUN pip3 install -r requirements.txt \
    && apt-get update \
    && apt-get install netcat-openbsd -y

ENTRYPOINT sudo chmod +x wait.sh \
    && sudo ./wait.sh \
    && sudo chmod +x run_python\
    && sudo sh run_python.sh
EXPOSE 8000