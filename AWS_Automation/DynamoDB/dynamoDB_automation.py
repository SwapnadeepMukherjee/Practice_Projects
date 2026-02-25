# Topic: ProvisionedThroughputExceededException

# Enable SDK Retry with Exponential Backoff. DynamoDB is designed to work with retries.

from botocore.config import Config
import boto3

config = Config(
    region_name='ap-south-1',
    retries={
        'max_attempts': 10,
        'mode': 'adaptive'
    }
)

dynamodb = boto3.resource('dynamodb', config=config)

