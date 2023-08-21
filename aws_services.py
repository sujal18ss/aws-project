import boto3

myEc2 = boto3.client("ec2")

#for launching
def ec2_launch():
    response = myEc2.run_instances(ImageId='ami-0ded8326293d3201b',
                    InstanceType='t2.micro',
                    MaxCount=1,
                    MinCount=1
                    )


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
            

def s3_bucket():
    myBucket = boto3.client('s3')
    myBucket.create_bucket(
        Bucket='lw-cloud-burst-22',
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'}
        )   
    
def list_s3_bucket():
    s3_buckets = boto3.client("s3")
    print("\nListing S3 buckets...")
    response = s3_buckets.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket["Name"])
        

# ec2_launch()
# list_ec2_instances()
# s3_bucket()
# list_s3_bucket()
