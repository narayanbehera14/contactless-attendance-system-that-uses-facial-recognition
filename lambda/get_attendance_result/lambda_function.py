import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("RecognitionResults")


def lambda_handler(event, context):

    params = event.get("queryStringParameters")

    if not params or "key" not in params:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Missing image key"
            })
        }

    image_key = params["key"]

    response = table.get_item(
        Key={
            "image_key": image_key
        }
    )

    if "Item" not in response:
        return {
            "statusCode": 404,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Recognition result not found"
            })
        }

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response["Item"])
    }
