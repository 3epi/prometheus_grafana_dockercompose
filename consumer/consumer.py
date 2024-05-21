from kafka import KafkaConsumer
import time

def consume_messages(bootstrap_servers, topic, group_id='your_group'):
    while True:
        try:
            consumer = KafkaConsumer(topic,
                                     group_id=group_id,
                                     bootstrap_servers=bootstrap_servers)
            print(f"Connected to Kafka brokers at {bootstrap_servers} and consuming topic {topic}")
            for message in consumer:
                print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
        except Exception as e:
            print(f"Error connecting to Kafka brokers: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

bootstrap_servers = 'kafka:9092'
topic = 'mytopic'

consume_messages(bootstrap_servers, topic)
