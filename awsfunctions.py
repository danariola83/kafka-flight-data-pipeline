import boto3
import json
from s3fs import S3FileSystem

def get_session_credentials():
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()

    credentials_dict = {
        "aws_access_key_id": credentials.access_key,
        "aws_secret_access_key": credentials.secret_key,
        "aws_session_token": credentials.token
    }
    
    return credentials_dict

def get_EC2_dns():
    #for kafka-flight-data-streaming instance
    instance_id =  'i-01925783295bff25a'

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    response_json = json.dumps(response, indent=4, sort_keys=True, default=str)

    ec2_dns = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicDnsName']

    return ec2_dns

def load_to_S3(msg, country, bucket_name):
    s3 = S3FileSystem()

    for i in msg:
        with s3.open("s3://{}/{}_air_traffic_{}_{}.json".format(bucket_name, country, i['api_call_timestamp'], i['callsign']), 'w') as file:
            json.dump(i, file, indent=4)

