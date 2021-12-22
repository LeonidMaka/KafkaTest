from kafka import KafkaConsumer

consumer = KafkaConsumer('chisla')
for message in consumer:
    print(message.value.decode('UTF-8'))
