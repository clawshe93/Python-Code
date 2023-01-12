#Get All EC2 Instance IDs
import boto3

ec2_client = boto3.client('ec2')
x = ec2_client.describe_instances()
x.keys()
len(x['Reservations'])
data = x['Reservations'][0]
data_instance = data['Instances']

print (len(data_instance))

for i in range(len(data_instance)):
   print(f"Instance ID is {data_instance[i]['InstanceId']}")
