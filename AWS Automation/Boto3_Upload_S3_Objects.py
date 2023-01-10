import boto3
s3_resource = boto3.client('s3')
s3_resource.upload_file(
    Filename='upload.png',
    Bucket='cpthegenius',
    Key='uploadtest.png',
    ExtraArgs=None,
    Callback=None,
    Config=None,
)