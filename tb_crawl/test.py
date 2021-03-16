# #-*— coding:utf-8 -*-
# import requests
#
# def get_file():
#     headers={
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#         "Cookie": "cgptmhCookie=mh_ymouejl6oos7hd03gq5h30dcxl2oc8imeohs; st=f5254bb082a6996796a328e99efdc0af; AlteonPcgmh=0a03b7f2718a9b7e1f41",
#         "Authorization" :"f5254bb082a6996796a328e99efdc0af",
#     }
#     # url="https://cg.95306.cn/proxy/portal/elasticSearch/indexView?noticeId=d80e45a6-9976-4c01-aa32-d69bc6d24eaa"
#     url="https://cg.95306.cn/proxy/portal/elasticSearch/indexView?noticeId=3ae96d16-879a-4950-9c3a-f7b61e410411"
#     response=requests.get(url,headers=headers)
#     print(response.text)
# def main():
#     get_file()
#
# if __name__=="__main__":
#     main()
import json

data = {
    "isWeakPwd": "0",
    "loginDevice": "mac",
    "loginMedia": "Chrome: 86.0.4240.198",
    "loginType": 3,
    "requestFlag": "acaea443f5c484a7c4b29ae42f09a204",
    "returnUrl": "https://cg.95306.cn/",
    "rndCode": "ABE8D76E446CFE3D6939FA716C9A276C",
    "userAccount": "henandeyou",
    "userPassword": "4EEDC48F39B9D37FB19B9B7A5EAEC5FF"
}

data=json.dump(data)
print(data)