from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps, loads

def kafka_Produce(dns, event, topic):
    producer = KafkaProducer(
        bootstrap_servers=[f'{dns}:9092'], 
        api_version=(0,10,2),
        value_serializer=lambda x:dumps(x).encode('utf-8')
        )
    
    producer.send(topic, value=event)

def kafka_Consume(dns, event, topic):
    consumer = KafkaConsumer(
        topic, 
        api_version=(0,10,2), 
        bootstrap_servers=[f'{dns}:9092'],
        group_id=None,  
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=10000
        )
    
    return consumer