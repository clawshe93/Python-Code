import boto3

ec2_resource=boto3.resource('ec2')
ec2_resource.create_instances(ImageId='ami-0b0dcb5067f052a63',
    InstanceType='t2.micro',
    SubnetId= 'subnet-092f222bb8cbd8e22',
    MaxCount=3,
    MinCount=3)