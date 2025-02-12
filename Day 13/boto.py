import boto3
client = boto3.client('s3')

response = client.create_bucket(
    Bucket='vk-demo-boto3-123',
)

print(response)