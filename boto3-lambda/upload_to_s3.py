#!/usr/bin/python3
from argparse import  ArgumentParser
from botocore.client import ClientError
import boto3
import time
import sys
    

def create_bucket(bucketnm):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucketnm)
    except ClientError:
        bucket = s3.create_bucket(Bucket=bucketnm)

def upload_file_to_s3(client,inf, bn, fn):
    client.upload_fileobj(inf, bn,fn)


def main():
    parser = ArgumentParser()
    parser.add_argument('filename', help='file name:')
    parser.add_argument('bucketname', help='input s3 bucekt name: ')
    args = parser.parse_args()
    print(args)
    
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

    client = boto3.client('s3')
    create_bucket(args.bucketname)
    fn = f"{timestamp}-{args.filename}"
    inf = open(args.filename, 'rb')
    upload_file_to_s3(client, inf, args.bucketname, fn)

if __name__ == '__main__':
    sys.exit(main()) 
