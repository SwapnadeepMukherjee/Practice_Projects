import boto3
import os
from datetime import datetime
import tempfile

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# LOCAL_LOG_FILE = os.path.join(BASE_DIR, 'app_log.txt')
BUCKET_NAME = "s3-swapnadeep-bucket-origin-v2"
# LOCAL_LOG_FILE = 'app_log.txt'
LOCAL_LOG_FILE =r'D:\Career\Personal_Study_Data\Github_Master\Practice_Projects\AWS_Automation\app_log.txt'
DOWNLOAD_DIR = tempfile.gettempdir()

s3 = boto3.client('s3')

# folder = r"D:\Career\Personal_Study_Data\Github_Master\Practice_Projects\AWS_Automation"

# print("Files inside folder:")
# for f in os.listdir(folder):
#     print(repr(f))

# Upload log file to S3:
print("Uploading log file to S3...")
s3.upload_file(LOCAL_LOG_FILE, BUCKET_NAME, os.path.basename(LOCAL_LOG_FILE))
print("Upload complete.")

#Listing files in S3 bucket:
print("Listing files in S3 bucket...")
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

if 'Contents' in response:
    for obj in response['Contents']:
        print(f" - {obj['Key']} (Last Modified: {obj['LastModified']})") 
else:
    print("No files found in the bucket.")

# Download latest log file from S3:
print("Downloading latest log file from S3...")
if 'Contents' in response:
    latest_file = max(response['Contents'], key=lambda x: x['LastModified'])
    s3.download_file(BUCKET_NAME, latest_file['Key'], os.path.join(DOWNLOAD_DIR, latest_file['Key']))
    # print(f"Downloaded {latest_file['Key']} to {DOWNLOAD_DIR}")

    latest_key = latest_file['Key']
    print(f"Latest file downloaded: {latest_key}")

    download_file_path = os.path.join(DOWNLOAD_DIR, latest_key)
    print(f"Downloaded file path: {download_file_path}")
    s3.download_file(BUCKET_NAME, latest_key, download_file_path)
    print(f"Downloaded {latest_key} to {download_file_path}")