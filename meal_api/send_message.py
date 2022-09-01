import requests
import json
import values

def send_message_object(data):
    headers=values.access_token()

    data = {'template_object': json.dumps(data)} 
    response = requests.post(values.default_send_url, headers=headers, data=data)
    return response.status_code

def send_message_id(id,args):
    headers=values.access_token()

    data = {'template_id': str(id),'template_args':json.dumps(args)} 
    response = requests.post(values.send_url, headers=headers, data=data)
    return response.status_code