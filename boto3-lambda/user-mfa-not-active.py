#!/usr/bin/env python3

import boto3

client = boto3.client('iam')
iam_users = []
response = client.list_users()
for user in response['Users']:
    iam_users.append(user['UserName'])
while 'Marker' in response:
    response = client.list_users(Marker=response['Marker'])
    for user in response['Users']:
        iam_users.append(user['UserName'])

no_mfa_users = []
for iam_user in iam_users:
    response = client.list_mfa_devices(UserName=iam_user)
    if not response['MFADevices']:
        no_mfa_users.append(iam_user)

print(no_mfa_users)
