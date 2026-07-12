import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("RecognitionResults")


def lambda_handler(event, context):

    key = event["queryStringParameters"]["key"]

    response = table.get_item(
        Key={
            "image_key": key
        }
    )

    if "Item" not in response:

        return {
            "statusCode": 404,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps({
                "message": "Result not ready"
            })
        }

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps(response["Item"])
    }
