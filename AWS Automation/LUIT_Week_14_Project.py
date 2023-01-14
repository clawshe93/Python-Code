import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')

instances = ['i-0534842151dcbe2ad', 'i-096b5311fe917c609', 'i-0ae46364138c0ca7a']
ec2_client.stop_instances(InstanceIds=instances)

print('stopped your instance(s)')

