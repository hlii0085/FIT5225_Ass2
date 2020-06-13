import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    """
        This function is the lambda function to Find Query
        When a JSON object query request, this function will be called
        After finding in the database, a response contains the list of URLs will be returned
        """
    tagggs = event["tags"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('images')
    response = table.scan()
    item = response["Items"]

    try:

        output_dict = {}
        links = []
        response = {}

        for d in item:
            match = 0
            b = []
            for tag in d["tags"]:
                if tag not in b:
                    for query in tagggs:
                        if tag == query:
                            match += 1
                            b.append(tag)
                            if match == len(tagggs):
                                links.append(d["url"])

        output_dict = {"links": links}

        if len(links) == 0:
            return json.dumps("Sorry, we did not find any image with all the tag(s) you entered")
        else:
            return json.dumps(output_dict)

    except Exception as e:
        print(e)
        raise e







