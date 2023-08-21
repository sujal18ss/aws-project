#!/usr/bin/python3

import boto3

def list_ec2_instances():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")  # Change the region as needed

    print("\nListing EC2 instances...")

    response = ec2_client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]

            print(f"Instance ID: {instance_id}, Instance Type: {instance_type}, State: {state}")