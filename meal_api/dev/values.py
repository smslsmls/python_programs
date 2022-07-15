from os import path
import json
import datetime

token_url = 'https://kauth.kakao.com/oauth/token'
unlink_url="https://kapi.kakao.com/v1/user/unlink" 
default_send_url="https://kapi.kakao.com/v2/api/talk/memo/default/send" 
send_url="https://kapi.kakao.com/v2/api/talk/memo/send" 

rest_api_key = '0af09b18c6e4e045fe7ceb4ddcc50845'
javascript_key = 'f62525eceb0ce9a158e28970199ffd89'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'YMlNfG2__SVkZ6BK-9XOsYfKCJt1gYBZWFPK4nOWHxBmRB-t4-g4aPHWkVkTJKTxDh5trgopb9QAAAF_2Phxpg'

authorization_data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
}

dir=path.split(path.abspath(__file__))[0]

kakao_json=dir+'\\kakao_code.json'

refresh_token=dir+'\\refresh_token.txt'

value_json=dir+'\\value.json'

meal_data=dir+'\\meal_data.json'

meal_name = ['조식', '중식', '석식']

def access_token():
    with open(kakao_json,"r") as kakao: 
        tokens = json.load(kakao) 

    headers={
        "Authorization" : "Bearer " + tokens["access_token"] 
    } 

    return headers

def time_str():
    now=datetime.datetime.now().date()
    res=str(now.year)
    res+='-'
    if now.month<10:
        res+='0'
    res+=str(now.month)
    res+='-'
    if now.day<10:
        res+='0'
    res+=str(now.day)
    return res