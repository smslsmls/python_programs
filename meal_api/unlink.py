import requests
import values

def unlink():
    headers=values.access_token()

    response = requests.post(values.unlink_url, headers=headers)
    print(response.status_code)