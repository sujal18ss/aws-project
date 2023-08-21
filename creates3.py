#!/usr/bin/python3

import boto3

def s3_bucket():
    myBucket = boto3.client('s3')
    myBucket.create_bucket(
        Bucket='lw-cloud-burst-22',
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'}
        )   
 