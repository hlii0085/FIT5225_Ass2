import boto3
import json
import numpy as np
import cv2 as cv

confThreshold = 0.5
inpWidth = 320
inpHeight = 320
names_file = open('coco.names', 'rt')
# Return a list of objects' names
names = names_file.read().rstrip('\n').split('\n')
yolo_weights = 'yolov3.weights'
yolo_cfg = 'yolov3.cfg'
image_base_url = 'https://tag-store-bucket.s3.amazonaws.com/'
table_name = 'images'


def lambda_handler(event, context):
    """
    This function is the lambda function for doing the object detection
    When there is a image upload into the S3 bucket,
    this function will be called
    After the detection, tags with url will insert into DynamoDB
    """
    bucket = event['Records'][0]['s3']['bucket']['name']

    key = event['Records'][0]['s3']['object']['key']

    s3 = boto3.client("s3")

    dynamodb = boto3.client('dynamodb')

    try:
        s3_response = s3.get_object(Bucket=bucket, Key=key)

        print(s3_response)

        image = s3_response['Body'].read()

        cfg = s3.get_object(Bucket=bucket, Key=yolo_cfg)['Body'].read()

        weights = s3.get_object(Bucket=bucket, Key=yolo_weights)['Body'].read()

        result_dict = do_detection(image, cfg, weights)

        result_dict['url'] = image_base_url + key

        print(json.dumps(result_dict))

        item = {}

        item["url"] = {"S": image_base_url + key}

        tags = []

        for tag in result_dict["tags"]:
            tags.append({"S": tag})

        item["tags"] = {"L": tags}

        db_response = dynamodb.put_item(TableName=table_name, Item=item)

        print(db_response)

    except Exception as e:
        print(e)
        raise e


def do_detection(file, cfg, weights):
    # file = request.files["image"].read()
    image = np.asarray(bytearray(file), dtype="uint8")
    image = cv.imdecode(image, cv.IMREAD_COLOR)
    blob = cv.dnn.blobFromImage(image, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)

    # net cannot share between threads
    # To load model, config file and name file for initialization
    net = cv.dnn.readNetFromDarknet(cfg, weights)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))

    # key: 'tags' value: list of tags
    tags = []
    result_dict = dict()
    for out in outs:
        for detection in out:
            scores = detection[5:]
            # the index of the highest confidence
            classId = np.argmax(scores)
            # assign highest confidence to 'confidence' using value at index 'classId' of 'scores' array
            confidence = scores[classId]
            # do filtering job
            if confidence > confThreshold:
                tags.append(names[classId])

    result_dict['tags'] = tags

    return result_dict


def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
