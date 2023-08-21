#!/usr/bin/python3

import boto3

def list_s3_bucket():
    s3_buckets = boto3.client("s3")
    print("\nListing S3 buckets...")
    response = s3_buckets.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket["Name"])