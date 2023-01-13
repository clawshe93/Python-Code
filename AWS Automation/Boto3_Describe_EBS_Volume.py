import boto3

client = boto3.client('ec2')
response = client.describe_volumes()

data = response['Volumes']
print(len(data)) 

for volume in data:
    device=volume["Attachments"]
    print(device) 
