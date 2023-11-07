FROM python:3.11

RUN apt-get install -y curl
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install djangorestframework
