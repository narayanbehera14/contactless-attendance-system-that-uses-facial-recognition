import boto3
import json
import uuid

s3 = boto3.client("s3")

BUCKET = "narayan-attendance-system-2026"

def lambda_handler(event, context):

    filename = f"uploads/{uuid.uuid4()}.jpg"

    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": BUCKET,
            "Key": filename,
            "ContentType": "image/jpeg"
        },
        ExpiresIn=300
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps({
            "uploadUrl": url,
            "key": filename
        })
    }


    
