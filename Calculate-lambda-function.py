import boto3
from datetime import datetime
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CalculatorResults')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        expression = body['expression']

        # Evaluate the expression
        result = eval(expression)

        # Get the current timestamp
        timestamp = str(datetime.now())

# Store the calculation and result in DynamoDB
        table.put_item(
            Item={
                'calculation_id': timestamp,
                'expression': expression,
                'result': str(result),
                'timestamp': timestamp
            }
        )
      

        response = {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response
