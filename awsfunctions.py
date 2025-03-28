import boto3
import json
from s3fs import S3FileSystem

def get_EC2_dns():
    #for kafka-flight-data-streaming instance
    instance_id =  'i-01925783295bff25a'

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    response_json = json.dumps(response, indent=4, sort_keys=True, default=str)

    ec2_dns = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicDnsName']

    return ec2_dns