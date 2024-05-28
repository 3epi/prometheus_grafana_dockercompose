from kafka import KafkaConsumer
import time
import pymongo

def consume_messages(bootstrap_servers, topic, mycol , group_id='your_group'):
    batch = []
    
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
                datadict = {
                    "topic" : message.topic,
                    "partition" : message.partition,
                    "offset" : message.offset,
                    "key" : message.key ,
                    "value" : message.value
                }
                batch.append(datadict)
                
                if len(batch) >= 50:
                    mycol.insert_many(batch)
                    batch = []
        
        except Exception as e:
            print(f"Error connecting to Kafka brokers: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)        
    
    if batch:
        mycol.insert_many(batch)
        batch = []
        

bootstrap_servers = 'kafka:9092'
topic = 'mytopic'

client = pymongo.MongoClient("mongo", 27017)
mydb = client["mydatabase"]
mycol = mydb["consumeddata"]
consume_messages(bootstrap_servers, topic , mycol)
