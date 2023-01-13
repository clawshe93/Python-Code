import boto3

client = boto3.client('ec2')
client.create_volume(AvailabilityZone='us-east-1a',
    Size=8,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Tutorial38'
                },
            ]
            
        },
    ],
)
