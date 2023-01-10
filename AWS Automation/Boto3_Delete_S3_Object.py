import boto3

s3_resource = boto3.client('s3')
object = s3_resource.delete_object(Bucket="cpthegenius",
    Key="Phone Ringing Noise.mp3")

