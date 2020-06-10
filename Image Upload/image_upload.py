import json
import base64
import boto3
import time


def lambda_handler(event, context):
    """
    This function is the lambda function for uploading the image via API gateway
    When a http POST request with the image in its body is sent to the gateway it will called this function
    """
    s3 = boto3.client("s3")

    image = event["content"]

    decode_image = base64.b64decode(image)

    millis = int(round(time.time() * 1000))
    s3_upload = s3.put_object(Bucket="tag-store-bucket", Body=decode_image, Key=str(millis) + '.jpg')

    return {
        'statusCode': 200,
        'body': json.dumps('image uploaded!'),
        'headers': {
            'Access-Control-Allow-Headers': '*'
        },
        
    }

