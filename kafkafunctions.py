from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

def kafka_Produce(dns, event, topic):
    producer = KafkaProducer(
        bootstrap_servers=[f'{dns}:9092'], 
        api_version=(0,10,2),
        request_timeout_ms=60000,
        value_serializer=lambda x:dumps(x).encode('utf-8')
        )

    producer.send(topic, value=event)

def kafka_Consume(dns, topic):
    consumer = KafkaConsumer(
        topic, 
        api_version=(0,10,2), 
        bootstrap_servers=[f'{dns}:9092'],
        group_id=None,  
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=20000
        )
    
    for msg in consumer:
        return msg.value