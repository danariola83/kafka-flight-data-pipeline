from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps, loads

# class KafkaFlight:
#     def __init__(self, dns, topic, event):
#         self.dns = dns
#         self.topic = topic
#         self.event = event
#         self.producer = KafkaProducer()
#         self.consumer = KafkaConsumer()


#------------------ v1.1 test ------------------#
# def __init__(self, dns, topic, event):
#     self.dns = dns
#     self.topic = topic
#     self.event = event
    
# def kafka_Produce(self):
#     producer = KafkaProducer(
#         bootstrap_servers = [f'{self.dns}:9092'], 
#         api_version = (0,10,2),
#         value_serializer = lambda x:dumps(x).encode('utf-8')
#         )
    
#     producer.send(self.topic, value=self.event)

# def kafka_Consume(self):
#     consumer = KafkaConsumer(
#         self.topic, 
#         api_version = (0,10,2), 
#         bootstrap_servers = [f'{self.dns}:9092'],
#         group_id = None,  
#         value_deserializer = lambda x: loads(x.decode('utf-8')),
#         consumer_timeout_ms = 15000
#         )
    
#     return consumer

# def kafka_Generate(self):
#     consumer = self.kafka_Consume()
#     self.kafka_Produce

#     return consumer


#------------------ v1.0 ------------------#
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
        consumer_timeout_ms=15000
        )
    
    for msg in consumer:
        return msg.value