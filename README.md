# IoT Device Simulator

This project simulates IoT device readings and stores them in DynamoDB.  
It also sends custom metrics to CloudWatch for monitoring.

## Features
- Simulates temperature and humidity readings
- Writes readings to DynamoDB
- Sends CloudWatch custom metrics (`Temperature`, `Humidity`, `ReadingsSent`)
- Fully serverless using AWS Lambda

## Usage
1. Deploy `lambda_function.py` to AWS Lambda.
2. Attach an IAM role with:
   - DynamoDB write access
   - CloudWatch `PutMetricData` access
3. Test Lambda manually or schedule with EventBridge.
4. Monitor metrics in CloudWatch.

## Requirements
- Python 3.13+
- boto3
