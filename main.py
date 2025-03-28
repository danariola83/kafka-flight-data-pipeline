from airtraffic import AirTraffic as atfc
from bbox import get_min_bbox, get_max_bbox

import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json
import boto3


EC2_dns = ''
producer = KafkaProducer(bootstrap_servers=[f'{EC2_dns}:9092'], 
                         api_version=(0,10,2),
                         value_serializer=lambda x:dumps(x).encode('utf-8'))

country = "Philippines"
lon_min,lat_min = get_min_bbox(country)
lon_max,lat_max = get_max_bbox(country)
user_name = ''
password = ''

flights = atfc(lon_min, lat_min, lon_max, lat_max, user_name, password, country)
flights_df = flights.get_flights_df()
flights_json = flights_df.to_dict(orient='records')
producer.send('EC2_ip_test1', value=flights_json)

print(flights_df)