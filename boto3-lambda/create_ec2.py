#!/usr/bin/python3

import boto3

ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId = 'ami-02e136e904f3da870',
    InstanceType = 't2.micro',
    KeyName='ec2-key-name',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
        'ResourceType': 'instance',
        'Tags': [
            {
            'Key': 'Name',
            'Value': 'pluto-bk'
            },
            {
            'Key': 'Owner',
            'Value': 'hz028'
            },
            {
            'Key': 'Backup',
            'Value': 'Yes'
            }
        ]
    }]
)
