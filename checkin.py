import requests
import json
import pandas as pd



def GLaDOS_Checkin():
    url = "https://glados.rocks/api/user/checkin"

    checkin_data = {"token": "glados_network"}
    checkin_data_json = json.dumps(checkin_data)
    headers = {"Content-Type": "application/json;charset=utf-8",
               "cookie": "_ga=GA1.2.1711711011.1647243913; _gid=GA1.2.585600631.1647243913; koa:sess=eyJ1c2VySWQiOjEwNDg3NCwiX2V4cGlyZSI6MTY3MzE2NDA5MTUxMiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=y7r_SxXn407qBux4sRfS4LEHGLE"
               }

    requests.packages.urllib3.disable_warnings()
    response = requests.request("POST", url, data=checkin_data_json, headers=headers, verify=False)
    print(response.text)


    

if __name__ == '__main__':
    GLaDOS_Checkin()
