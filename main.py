from airtraffic import AirTraffic
from bbox import get_min_bbox, get_max_bbox
from awsfunctions import get_EC2_dns, load_to_S3
from kafkafunctions import kafka_Produce, kafka_Consume
from concurrent.futures import ThreadPoolExecutor

instance_id = 'i-0755203d7564e5adc'
EC2_dns = get_EC2_dns(instance_id)
S3_bucket = 'kafka-flight-data'
topic = 'flight_data'

country = "Philippines"
lon_min,lat_min = get_min_bbox(country)
lon_max,lat_max = get_max_bbox(country)
user_name = ''
password = ''

flights = AirTraffic(lon_min, lat_min, lon_max, lat_max, user_name, password, country)
flights_df = flights.get_flights_df()
flights_json = flights_df.to_dict(orient='records')

# concurrently running kafka functions as futures
msg = None

with ThreadPoolExecutor(max_workers=5) as executor:
    f_Consumer = executor.submit(kafka_Consume, EC2_dns, topic)
    f_Producer = executor.submit(kafka_Produce, EC2_dns, flights_json, topic)
    
    # assigns a list of flight dicts returned from kafka_Consume function to msg
    msg = f_Consumer.result()


# load each dict in msg as individual json in s3
load_to_S3(msg, country, S3_bucket)

