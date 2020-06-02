"""
This model provides a mechanism to upload an image to an S3 bucket.
    1. API Gateway or AWS SDKs(boto3)
    2. Whenever an image is uploaded to the S3 bucket,
       the system must trigger an event and thus invoke a Lambda function to do object detection
    3. The Lambda function should read the uploaded image and detect objects in the image
    4. Finally, save the list of detected objects along with the S3-url in an AWS database
"""
