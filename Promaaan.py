from kafka import KafkaProducer
from random import randint
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
while (True):
    value=str(randint(10,10000))
    producer.send('chisla', value.encode('UTF-8'))
    time.sleep(2)
