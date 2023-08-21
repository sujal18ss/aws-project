#!/usr/bin/python3

import boto3

#for launching
def ec2_launch():
    myEc2 = boto3.client("ec2")
    response = myEc2.run_instances(ImageId='ami-0ded8326293d3201b',
                    InstanceType='t2.micro',
                    MaxCount=1,
                    MinCount=1
                    )
