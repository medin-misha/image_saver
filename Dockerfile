FROM python:3.12

RUN sudo apt install nginx  
COPY nginx.conf /etc/nginx

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ app/
