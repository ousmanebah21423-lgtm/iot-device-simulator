import boto3
import random
import uuid
import logging
from datetime import datetime, timezone
from decimal import Decimal

# Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("IoTDeviceReadings")

# CloudWatch setup
cloudwatch = boto3.client("cloudwatch")

def lambda_handler(event, context):
    # Generate a simulated IoT reading
    reading = {
        "DeviceID": str(uuid.uuid4()),
        "Timestamp": datetime.now(timezone.utc).isoformat(),
        "Temperature": Decimal(str(random.uniform(20, 30))),
        "Humidity": Decimal(str(random.uniform(30, 60))),
    }

    # Store reading in DynamoDB
    table.put_item(Item=reading)
    logger.info(f"Sent reading: {reading}")

    # Publish custom CloudWatch metrics
    cloudwatch.put_metric_data(
        Namespace='IoTDeviceSimulator',
        MetricData=[
            {
                'MetricName': 'ReadingsSent',
                'Dimensions': [
                    {'Name': 'DeviceID', 'Value': reading['DeviceID']}
                ],
                'Unit': 'Count',
                'Value': 1
            },
            {
                'MetricName': 'Temperature',
                'Dimensions': [
                    {'Name': 'DeviceID', 'Value': reading['DeviceID']}
                ],
                'Unit': 'None',
                'Value': float(reading['Temperature'])
            },
            {
                'MetricName': 'Humidity',
                'Dimensions': [
                    {'Name': 'DeviceID', 'Value': reading['DeviceID']}
                ],
                'Unit': 'None',
                'Value': float(reading['Humidity'])
            }
        ]
    )

    # Return Lambda success
    return {
        "statusCode": 200,
        "body": "IoT reading stored and metrics sent successfully"
    }
