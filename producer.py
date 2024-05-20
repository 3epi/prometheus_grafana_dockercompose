import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

def create_kafka_producer(bootstrap_servers, max_retries=3, retry_interval=5):
    for attempt in range(1, max_retries + 1):
        try:
            return KafkaProducer(bootstrap_servers=bootstrap_servers)
        except NoBrokersAvailable:
            print(f"Attempt {attempt}: No brokers available. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
    raise RuntimeError("Failed to connect to Kafka brokers after multiple attempts.")

# Define Kafka bootstrap servers
bootstrap_servers = 'localhost:9092'

# Create Kafka producer with retry mechanism
producer = create_kafka_producer(bootstrap_servers)

# Produce message to Kafka topic
producer.send('mytopic', b"test message")
producer.flush()

print("Message sent to Kafka!")

# Close the Kafka producer
producer.close()
