#!/usr/bin/python3

import boto3

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

print(f'Instances with Tag:')
for instance in instances:
    print(f'  - Instance ID: {instance.id}')
~                                               
