from airtraffic import AirTraffic as atfc
from bbox import get_min_bbox, get_max_bbox
from awsfunctions import get_EC2_dns
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

EC2_dns = get_EC2_dns()
topic = 'EC2_ip_test1'

country = "Philippines"
lon_min,lat_min = get_min_bbox(country)
lon_max,lat_max = get_max_bbox(country)
user_name = ''
password = ''

flights = atfc(lon_min, lat_min, lon_max, lat_max, user_name, password, country)
flights_df = flights.get_flights_df()
flights_json = flights_df.to_dict(orient='records')

producer = KafkaProducer(
    bootstrap_servers=[f'{EC2_dns}:9092'], 
    api_version=(0,10,2),
    request_timeout_ms=60000,
    value_serializer=lambda x:dumps(x).encode('utf-8')
    )

producer.send(topic, value=flights_json)
# producer.send(topic, value={"test":"json"})
# producer.flush()

