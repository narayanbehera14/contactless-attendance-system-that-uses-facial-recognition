import boto3
import os

rekognition = boto3.client("rekognition")

COLLECTION_ID = "employee-attendance"

def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    employee_id = os.path.basename(key).split(".")[0]

    response = rekognition.index_faces(
        CollectionId=COLLECTION_ID,
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        },
        ExternalImageId=employee_id,
        DetectionAttributes=[]
    )

    return {
        "statusCode": 200,
        "body": str(response)
    }
