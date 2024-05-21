import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

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
    producer.send('mytopic', b"test message")
    print("message sent")
    producer.flush()

producer.close()
