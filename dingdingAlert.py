# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=0b132c83586374cee0f23150314b45f53fd02657fc0c2d75b502661a45335e5e"
 
def msg(text):
    json_text= {
     "msgtype": "text",
        
        "text": {
            "content": text
        }，
		"at": {
         "atMobiles": [
             "18796083373"
         ], 
         "isAtAll": false
     }
    }
    print (requests.post(api_url,json.dumps(json_text),headers=headers).content)
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)