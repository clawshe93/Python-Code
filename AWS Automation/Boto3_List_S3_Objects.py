import boto3

s3_resource=boto3.client('s3')
objects=s3_resource.list_objects(Bucket="cpthegenius")["Contents"]

len(objects)
if len(objects)>0:
    print("object(s) exists")

for object in objects:
    print(object["Key"])

    