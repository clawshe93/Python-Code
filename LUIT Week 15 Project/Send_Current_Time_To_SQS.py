import json
import boto3

from datetime import datetime


def lambda_handler(event, context):

    time = datetime.now()
    current_time = time.strftime("%H:%M:%S %p")

    message = boto3.client('sqs')
    message.send_message(
        QueueUrl="https://sqs.REGION.amazonaws.com/xxxxxxxxxxxx/QueueName",
        MessageBody=current_time
    )
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }