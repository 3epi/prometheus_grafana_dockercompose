FROM docker.arvancloud.ir/python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY consumer.py /app/consumer.py

CMD ["python3", "/app/consumer.py"]
