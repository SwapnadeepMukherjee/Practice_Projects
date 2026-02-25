import boto3
import os

ACCOUNT_ID = "788531719687"
ROLE_NAME = "S3UploadRole"
BUCKET_NAME = "s3-swapnadeep-bucket-origin-v2"

sts_client = boto3.client('sts')

assumed_role = sts_client.assume_role(
    RoleArn=f"arn:aws:iam::{ACCOUNT_ID}:role/{ROLE_NAME}",
    RoleSessionName="S3UploadDownloadSession"
)

credentials = assumed_role['Credentials']

s3 = boto3.client(
    's3', 
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)

#upload a file to S3:
s3.upload_file('app_log.txt', BUCKET_NAME, 'app_log_txt')

# List objects in the bucket:
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

#Dowload the file from S3:
if 'Contents' in response:
    latest = max(response['Contents'], key=lambda x: x['LastModified'])
    s3.download_file(BUCKET_NAME, latest['Key'], f"/tmp/{latest['Key']}")
