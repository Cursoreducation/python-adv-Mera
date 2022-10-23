FROM python:3.8

COPY app.py /app/app.py

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

CMD ["python", "app.py"]