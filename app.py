import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def get_cost_data(start_str, end_str):
    try:

        client = boto3.client('ce', region_name='us-east-1')

        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_str,
                'End': end_str
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
        )

        results = []
        for group in response['ResultsByTime'][0]['Groups']:
            service = group['Keys'][0]
            amount = group['Metrics']['UnblendedCost']['Amount']
            unit = group['Metrics']['UnblendedCost']['Unit']
            results.append({'service': service, 'cost': f"{amount} {unit}"})

        return results

    except (NoCredentialsError, ClientError, Exception) as e:
        print(f"Error fetching cost data: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default last full month
    end = datetime.today().replace(day=1)
    start = (end - timedelta(days=1)).replace(day=1)
    start_str = start.strftime('%Y-%m-%d')
    end_str = end.strftime('%Y-%m-%d')

    if request.method == 'POST':
