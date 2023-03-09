# FROM dokken/ubuntu-22.04
FROM python:3.8-slim-buster

RUN apt-get update
RUN apt install curl psmisc -y
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY v2ray v2ray
COPY pop_checker.py pop_checker.py

CMD [ "python3", "pop_checker.py"]