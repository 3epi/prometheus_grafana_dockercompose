import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import random
import string
import time

def generate_random_string(length=random.randint(10 , 1000)):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def create_kafka_producer(bootstrap_servers, max_retries=10, retry_interval=5):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}: Trying to connect to Kafka brokers at {bootstrap_servers}...")
            producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
            print("Successfully connected to Kafka brokers.")
            return producer
        except NoBrokersAvailable:
            print(f"Attempt {attempt}: No brokers available. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
    raise RuntimeError("Failed to connect to Kafka brokers after multiple attempts.")

bootstrap_servers = 'kafka:9092'

# Create Kafka producer with retry mechanism
producer = create_kafka_producer(bootstrap_servers)

while (True):
    message = generate_random_string()
    producer.send('mytopic', message)
    print("{message} sent")
    time.sleep(5)
    producer.flush()

producer.close()
