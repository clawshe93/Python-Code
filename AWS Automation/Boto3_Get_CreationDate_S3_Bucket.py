import boto3
s3_resource = boto3.client("s3")
creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

print (creation_date.strftime("%d%m%y_%H:%M%s"))