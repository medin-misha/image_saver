FROM python:3.12

RUN apt update && apt install -y nginx
RUN useradd -r -u 101 -g root nginx

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY nginx.conf /etc/nginx
COPY app/ app/


WORKDIR /app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & nginx -g 'daemon off;'"]