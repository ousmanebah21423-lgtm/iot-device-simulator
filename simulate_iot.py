import boto3
import random
import uuid
import logging
import time
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

from datetime import datetime, timezone
from decimal import Decimal

# DynamoDB setup
dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
table = dynamodb.Table("IoTDeviceReadings")


def generate_reading():
    return {
        "DeviceID": str(uuid.uuid4()),
        "Timestamp": datetime.now(timezone.utc).isoformat(),
        "Temperature": Decimal(str(random.uniform(20, 30))),
        "Humidity": Decimal(str(random.uniform(30, 60))),
    }


def send_reading():
    reading = generate_reading()
    table.put_item(Item=reading)
    logger.info(f"Sent reading: {reading}")



if __name__ == "__main__":
    logger.info("Starting IoT device simulator...")

    while True:
        send_reading()
        time.sleep(5)  # send data every 5 seconds
