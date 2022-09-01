import requests
import json
import values

def get_token():
    response = requests.post(values.token_url, data=values.authorization_data)
    tokens = response.json()
    fp=open(values.refresh_token,'w',encoding='utf-8')
    fp.write(tokens["refresh_token"])
    print(tokens)

    with open(values.kakao_json,"w") as fp:
        json.dump(tokens, fp)