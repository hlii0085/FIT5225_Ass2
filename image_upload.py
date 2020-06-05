import json
"""
This model provides a mechanism to upload an image to an S3 bucket.
    1. API Gateway or AWS SDKs(boto3)
    2. Whenever an image is uploaded to the S3 bucket,
       the system must trigger an event and thus invoke a Lambda function to do object detection
    3. The Lambda function should read the uploaded image and detect objects in the image
    4. Finally, save the list of detected objects along with the S3-url in an AWS database
"""


"""
This function is the lambda function for doing the object detection
When there is a image upload into the S3 bucket,
this function will be called, passing the event details and the context
"""


def lambda_handler(event, context):
    # TODO implement
    print(event)
    return event;


"""
This function is the lambda function for uploading the image via API gateway
When a http POST request with the image in its body is sent to the gateway it will called this function
"""


import json
import base64
import boto3
import time


def lambda_handler(event, context):
    s3 = boto3.client("s3")

    image = event["content"]

    decode_image = base64.b64decode(image)

    millis = int(round(time.time() * 1000))
    s3_upload = s3.put_object(Bucket="tag-store-bucket", Body=decode_image, Key=str(millis) + '.jpg')

    return {
        'statusCode': 200,
        'body': json.dumps('image uploaded!')
    }