import json
import requests
url =""
headers = {
    "Content-Type":"application/json",
    "Charset":"utf-8"
}
requests_data ={
    "msgtype":"text",
    "text":{
        "content":"饿了吗？"
    },
    "at":{
        "atMobiles":[
        ],
        "isAtAll":True
    }
}
sendData = json.dumps(requests_data)
response = requests.post(url = url,headers=headers,data=sendData)
content = response.json()
print(content)