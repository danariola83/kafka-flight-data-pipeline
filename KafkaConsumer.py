from kafka import KafkaConsumer
from awsfunctions import get_EC2_dns
from time import sleep
from json import dumps, loads
from s3fs import S3FileSystem

EC2_dns = get_EC2_dns()
topic = 'EC2_ip_test1'

consumer = KafkaConsumer(
    topic, 
    api_version=(0,10,2), 
    bootstrap_servers=[f'{EC2_dns}:9092'],
    group_id=None,  
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=15000
    )

for msg in consumer:
    print(msg.value[0])
    
# s3 = S3FileSystem()

# for msg in consumer:
#     for i in msg.value:
#         with s3.open("s3://kafka-flight-data/{}_air_traffic_{}_{}.json".format(country, i['api_call_timestamp'], i['icao24']), 'w') as file:
#             json.dump(i.value, file)