FROM docker.arvancloud.ir/python:3.11

RUN pip3 install kafka-python six

COPY consumer.py /consumer.py

CMD ["python3", "/producer.py"]
