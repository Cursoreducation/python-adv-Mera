FROM python:3.8

COPY app.py /app/app.py

RUN apt install curl

WORKDIR /app

CMD ["python", "app.py"]