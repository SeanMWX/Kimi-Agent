import requests
import json
import random

class Agent:

    def __init__(self, token):
        self.token = token

    def chat(self, text):

        url = "https://kimi.moonshot.cn/api/chat"
        cookies = 'Bearer ' + self.token
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": cookies,
            "content-type": "application/json",
            "r-timezone": "Asia/Shanghai",
            "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        data = {
            "name": "KimiChat API",
            "is_example": False
        }

        r = requests.post(url, headers=headers, json=data)

        if r.status_code == 200:
            chatid = r.json()['id']

            data2 = {
                "messages": [
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                "refs": [],
                "use_search": True
            }
            url2 = 'https://kimi.moonshot.cn/api/chat/' + str(chatid) + '/completion/stream'
            r2 = requests.post(url=url2,json=data2,headers=headers)
            if r2.status_code == 200:

                url3 = 'https://kimi.moonshot.cn/api/chat/' + str(chatid) + '/segment/scroll'
                headers3 = {
                    "accept": "*/*",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "authorization": cookies,
                    "content-type": "application/json",
                    "r-timezone": "Asia/Shanghai",
                    "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "referrer": "https://kimi.moonshot.cn/chat/",
                    "referrerPolicy": "strict-origin-when-cross-origin"
                }
                data3 = {
                    "last": 50
                }

                r3 = requests.post(url3, headers=headers3, json=data3)
                
                if r3.status_code == 200:
                    result = r3.json()
                    content = result['items'][-1]['content']

                    url4 = "https://kimi.moonshot.cn/api/chat/" + str(chatid)
                    headers4 = {
                        "accept": "*/*",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                        "authorization": cookies,
                        "content-type": "application/json",
                        "r-timezone": "Asia/Shanghai",
                        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin"
                    }

                    r4 = requests.delete(url4, headers=headers4)
                    if r4.status_code == 200:
                        return content
                    else:
                        exit('ERROR_Number:4')
                        return None
                else:
                    exit('ERROR_Number:3')
                    return None
            else:
                exit('ERROR_Number:2')
                return None
        else:
            exit('ERROR_Number:1')
            return None