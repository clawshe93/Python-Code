import boto3

client = boto3.client('ec2')
x = client.describe_vpcs()

no_of_vpcs = x["Vpcs"]

print(len(no_of_vpcs))
for vpc in no_of_vpcs:
    print(vpc['VpcId'])
    
x2 = client.describe_vpcs(VpcIds = ["vpc-0532b1ccade3df12e"])

print(x2)