import requests
import json
import values

def f_auth_refresh():
    fp=open(values.refresh_token,'r',encoding='utf-8')
    r_token=fp.readline()
    data = { 
        "grant_type": "refresh_token", 
        "client_id": values.rest_api_key, 
        "refresh_token": r_token 
    } 
    with open(values.kakao_json, "r") as fp: 
        ts = json.load(fp) 
    response = requests.post(values.token_url, data=data) 
    tokens = response.json()

    with open(values.kakao_json, "w") as fp: 
        json.dump(tokens, fp) 

    with open(values.kakao_json, "r") as fp: 
        ts = json.load(fp)

    token = ts["access_token"] 
    return token
# print(f_auth_refresh())