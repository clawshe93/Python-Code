#Terminate multiple EC2 instances using Boto3
import boto3

ec2_client=boto3.client('ec2')
x=ec2_client.describe_instances()

print(len(x))
data = x['Reservations']

li=[]
for instances in data:
    instance=instances['Instances']
    for ids in instance:
        instance_id = ids['InstanceId']
        li.append(instance_id)
        
ec2_client.terminate_instances(InstanceIds=li)
