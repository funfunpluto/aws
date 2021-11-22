#!/usr/bin/python3

import boto3
from datetime import datetime

#AWS_REGION = "us-east-2"
EC2_RESOURCE = boto3.resource('ec2')
#INSTANCE_NAME_TAG_VALUE = 'my-ec2-instance'

instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'tag:Backup',
            'Values': [
                'Yes'
            ]
        }
    ]
)

timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

for i in instances.all():
    for v in i.volumes.all():
        desc = 'Backup of {0}, volume{1}, created {2}'.format(
            i.id, v.id, timestamp)
        print(desc)                                               
