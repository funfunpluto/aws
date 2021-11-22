#!/usr/bin/python3

import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances(Filters = [{'Name': 'key-name', 'Values':['ec2-key-name']}])
reservations = response.get("Reservations")
for res in reservations:
    for ins in res["Instances"]:

        if 'Tags' in ins.keys():
            for kpair in ins['Tags']:
                if kpair['Key'] == 'Backup' and kpair['Value'] == 'Yes':
                    print(ins["InstanceId"])
                    print(ins)


ec2 = boto3.resource('ec2')
print(ec2)
