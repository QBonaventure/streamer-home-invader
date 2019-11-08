import json
import os
from botocore.vendored import requests

def hello(event, context):

    try:
        challenge = event['queryStringParameters']['hub.challenge']

    except KeyError:
        type = event['queryStringParameters']['type']
        print(type)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        r = requests.post('http://'+os.environ['host_ip']+'/event_triggered?type='+type, headers=headers)


        return {
            'type': type,
            'res': r,
            'statusCode': 200,
            'body': 'OK'
        }

    else:
        return {
            'statusCode': 200,
            'body': challenge
        }
        
