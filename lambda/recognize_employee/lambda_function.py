import boto3
from datetime import datetime

rekognition = boto3.client("rekognition")
dynamodb = boto3.resource("dynamodb")

employees_table = dynamodb.Table("Employees")
attendance_table = dynamodb.Table("Attendance")

COLLECTION_ID = "employee-attendance"


def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    response = rekognition.search_faces_by_image(
        CollectionId=COLLECTION_ID,
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        },
        FaceMatchThreshold=95,
        MaxFaces=1
    )

    if not response["FaceMatches"]:
        return {
            "statusCode": 404,
            "message": "Unknown Person"
        }

    employee_id = response["FaceMatches"][0]["Face"]["ExternalImageId"]

    employee = employees_table.get_item(
        Key={
            "employee_id": employee_id
        }
    )

    if "Item" not in employee:
        return {
            "statusCode": 404,
            "message": "Employee Not Found"
        }

    employee = employee["Item"]

    now = datetime.now()

    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    attendance = attendance_table.get_item(
        Key={
            "employee_id": employee_id,
            "date": today
        }
    )

    # ---------- CLOCK IN ----------
    if "Item" not in attendance:

        attendance_table.put_item(
            Item={
                "employee_id": employee_id,
                "date": today,
                "clock_in": current_time,
                "clock_out": "",
                "status": "Present"
            }
        )

        return {
            "statusCode": 200,
            "employee": employee["name"],
            "status": "Clock In Successful",
            "time": current_time
        }

    # ---------- CLOCK OUT ----------

    attendance = attendance["Item"]

    if attendance["clock_out"] == "":

        attendance_table.update_item(
            Key={
                "employee_id": employee_id,
                "date": today
            },
            UpdateExpression="SET clock_out=:c",
            ExpressionAttributeValues={
                ":c": current_time
            }
        )

        return {
            "statusCode": 200,
            "employee": employee["name"],
            "status": "Clock Out Successful",
            "time": current_time
        }

    return {
        "statusCode": 200,
        "employee": employee["name"],
        "status": "Already Clocked Out Today"
    }

    

    
