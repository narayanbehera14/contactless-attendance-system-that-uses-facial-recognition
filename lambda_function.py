import boto3
from datetime import datetime

rekognition = boto3.client("rekognition")
dynamodb = boto3.resource("dynamodb")

employees_table = dynamodb.Table("Employees")
attendance_table = dynamodb.Table("Attendance")
results_table = dynamodb.Table("RecognitionResults")

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

    # ---------------- UNKNOWN PERSON ----------------

    if not response["FaceMatches"]:

        results_table.put_item(
            Item={
                "image_key": key,
                "status": "Unknown Person"
            }
        )

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

        results_table.put_item(
            Item={
                "image_key": key,
                "status": "Employee Not Found"
            }
        )

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

    # ---------------- CLOCK IN ----------------

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

        results_table.put_item(
            Item={
                "image_key": key,
                "employee_id": employee_id,
                "employee_name": employee["name"],
                "status": "Clock In Successful",
                "clock_in": current_time,
                "clock_out": ""
            }
        )

        return {
            "statusCode": 200,
            "employee": employee["name"],
            "status": "Clock In Successful",
            "time": current_time
        }

    attendance = attendance["Item"]

    # ---------------- CLOCK OUT ----------------

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

        results_table.put_item(
            Item={
                "image_key": key,
                "employee_id": employee_id,
                "employee_name": employee["name"],
                "status": "Clock Out Successful",
                "clock_in": attendance["clock_in"],
                "clock_out": current_time
            }
        )

        return {
            "statusCode": 200,
            "employee": employee["name"],
            "status": "Clock Out Successful",
            "time": current_time
        }

    # ---------------- ALREADY CLOCKED OUT ----------------

    results_table.put_item(
        Item={
            "image_key": key,
            "employee_id": employee_id,
            "employee_name": employee["name"],
            "status": "Already Clocked Out Today",
            "clock_in": attendance["clock_in"],
            "clock_out": attendance["clock_out"]
        }
    )

    return {
        "statusCode": 200,
        "employee": employee["name"],
        "status": "Already Clocked Out Today"
    }
