from kafka import KafkaConsumer

consumer = KafkaConsumer('monthly-report',
                         group_id='my-group',
                         bootstrap_servers=['kafka:29092'])
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))