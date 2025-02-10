import boto3
client = boto3.client('s3')

esponse = client.create_bucket(
    Bucket='first bucket'
)

