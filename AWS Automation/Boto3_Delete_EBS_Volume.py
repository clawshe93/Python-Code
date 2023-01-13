import boto3

ec2_client = boto3.client('ec2')
ec2_client.delete_volume(VolumeId='vol-028a215ce6c9dfa83')