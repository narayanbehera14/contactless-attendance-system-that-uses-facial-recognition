import boto3
import json
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Attendance")

def lambda_handler(event, context):

    today = datetime.now().strftime("%Y-%m-%d")

    response = table.scan()

    items = response["Items"]

    if not items:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "No attendance"})
        }

    latest = sorted(
        items,
        key=lambda x: x["clock_in"],
        reverse=True
    )[0]

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(latest)
    }
