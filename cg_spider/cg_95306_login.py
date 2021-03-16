# -*— coding:utf-8 -*-
import requests
import json

requests.packages.urllib3.disable_warnings()
from passport import pass_port
# 导入百度
from aip import AipOcr
import hashlib
session = requests.Session()
from redis import Redis
conn = Redis(host='', encoding='utf-8', port=6388,password='')

# class CgAuthorization(object):
#     def __init__(self,session):
#         # 获取requestFlag
#         self.requestFlag_url = "https://cg.95306.cn/proxy/passport/randInit/80404D0C6D24E87F650FF7D1985CD762"
#         # 获取三个图片验证码的url地址
#         self.rndCode1_url = "https://cg.95306.cn/proxy/passport/coordinate/v1/"
#         self.rndCode2_url = "https://cg.95306.cn/proxy/passport/coordinate/v2/"
#         self.rndCode3_url = "https://cg.95306.cn/proxy/passport/coordinate/v3/"
#         # 获取百度的API
#         self.APP_ID = '23622316'
#         self.API_KEY = 'CKLY4PUSdDIb2B9dZ1Aq9kzT'
#         self.SECRET_KEY = '1UT7IWFtmUVNDduUG8iGxllC7KKoDlTE'
#         # 登录
#         self.login_url = 'https://cg.95306.cn/proxy/passport/submit'
#         self.timeout = 5  #
#         self.session = session  # 共同存储session
#         # 用户 密码
#         self.userAccount = 'henandeyou'
#         self.userPassword = '4EEDC48F39B9D37FB19B9B7A5EAEC5FF'
#         self.headers = {
#             "cookie":"AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
#             "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#             "X-Requested-With":"XMLHttpRequest",
#             'Content-Type': 'application/json'
#         }
#         self.loginType = 3
#         self.loginMedia = "Chrome: 86.0.4240.198",
#         self.loginDevice = "mac",
#         self.isWeakPwd = "0"
#         self.returnUrl = "https://cg.95306.cn/"
#
#     def get_requestFlag(self):
#
#         # 获取参数requestFlag
#         try:
#             response = self.session.post(url=self.requestFlag_url, headers=self.headers, verify=False,
#                                         timeout=self.timeout)
#             response.raise_for_status()
#
#             Flag_json = json.loads(response.text)
#             print(Flag_json)
#         # 获取requsetFlag
#             requestFlag = Flag_json['data']
#             return requestFlag
#
#         except Exception as e:
#             print('检测是否获取requestFlag')
#             raise e
#
#     def get_rndcode(self):
#         requestFlag=self.get_requestFlag()
#         self.rndCode1_url = f"https://cg.95306.cn/proxy/passport/coordinate/v1/{str(requestFlag)}"
#         self.rndCode2_url = f"https://cg.95306.cn/proxy/passport/coordinate/v2/{str(requestFlag)}"
#         self.rndCode3_url = f"https://cg.95306.cn/proxy/passport/coordinate/v3/{str(requestFlag)}"
#
#
#
#         client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
#         #rndcode1 百度识别
#         rnd1=client.basicGeneralUrl(self.rndCode1_url).get('words_result')[0].get('words')
#         # #rndcode2百度识别
#         rnd2=client.basicGeneralUrl(self.rndCode2_url).get('words_result')[0].get('words')
#         # #rndcode3 百度识别
#         rnd3 =client.basicGeneralUrl(self.rndCode3_url).get('words_result')[0].get('words')
#         rndCode1 = pass_port.get(rnd1)
#         rndCode2 = pass_port.get(rnd2)
#         rndCode3 = pass_port.get(rnd3)
#         rndCode_first = requestFlag + rndCode1 + rndCode2 + rndCode3
#         return rndCode_first
#
#         # hex_md5方法
#     def hex_md5(self, str):
#         s=str.encode('utf-8')
#
#         md5_str=md5(s)
#         return md5_str.hexdigest()
#
#
#     #将rndcode加密
#     def hex_md5_wz(self):
#         renCode_first=self.get_rndcode()
#         self.rndCode = self.hex_md5(self.hex_md5(renCode_first).upper()).upper()
#         return self.rndCode
#
#     #登录
#     def get_login(self):
#         requestFlag = self.get_requestFlag()
#         rndCode=self.hex_md5_wz()
#         data={
#     	"loginType": self.loginType,
#     	"returnUrl": self.returnUrl,
#     	"requestFlag": requestFlag,
#     	"userAccount":self.userAccount,
#     	"userPassword": self.userPassword,
#     	"rndCode": rndCode,
#     	"loginMedia": self.loginMedia,
#     	"loginDevice":self.loginDevice,
#     	"isWeakPwd": self.isWeakPwd,
#     }
#         res=session.post(url=url,headers=headers,data=json.dumps(data),timeout=5,verify=False)
#         login_json=json.loads(res.text)
#         print(login_json)
#         Authorization=login_json['msg']
#         data_url=login_json['data']
#
#         print(Authorization,data_url)
#
# #
#
def get_requestFlag():
    #
    # 获取参数requestFlag
    try:
        headers = {
            "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            'Content-Type': 'application/json'
        }
        url = "https://cg.95306.cn/proxy/passport/randInit/80404D0C6D24E87F650FF7D1985CD762"
        response = session.post(url=url, headers=headers, verify=False,
                                     timeout=5)
        response.raise_for_status()

        Flag_json = json.loads(response.text)
        print(Flag_json)
        # 获取requsetFlag
        requestFlag = Flag_json['data']
        get_rndcode(requestFlag)
        # return requestFlag

    except Exception as e:
        get_requestFlag()
        print('检测是否获取requestFlag')
        raise e




def get_rndcode(requestFlag):
    rndCode1_url = f"https://cg.95306.cn/proxy/passport/coordinate/v1/{str(requestFlag)}"
    rndCode2_url = f"https://cg.95306.cn/proxy/passport/coordinate/v2/{str(requestFlag)}"
    rndCode3_url = f"https://cg.95306.cn/proxy/passport/coordinate/v3/{str(requestFlag)}"

    get_code(requestFlag, rndCode1_url, rndCode2_url, rndCode3_url)


def get_code(requestFlag, rndCode1_url, rndCode2_url, rndCode3_url):
    APP_ID = '23622316'
    API_KEY = 'CKLY4PUSdDIb2B9dZ1Aq9kzT'
    SECRET_KEY = '1UT7IWFtmUVNDduUG8iGxllC7KKoDlTE'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    print(client)
    # rndcode1 百度识别
    rnd1 = client.basicGeneralUrl(rndCode1_url).get('words_result')[0].get('words')
    print(rnd1, type(rnd1))

    # #rndcode2百度识别
    rnd2 = client.basicGeneralUrl(rndCode2_url).get('words_result')[0].get('words')
    # #rndcode3 百度识别
    rnd3 = client.basicGeneralUrl(rndCode3_url).get('words_result')[0].get('words')
    print(rnd1, rnd2, rnd3)

    rndCode1 = pass_port.get(rnd1)
    rndCode2 = pass_port.get(rnd2)
    rndCode3 = pass_port.get(rnd3)
    #
    #
    # #输出rendcode
    print(rndCode1, rndCode2, rndCode3)
    rndCode_first = requestFlag + rndCode1 + rndCode2 + rndCode3
    hex_md5_wz(requestFlag, rndCode_first)

    # js中hex_md5_wz 方法


def hex_md5(str):
    m = hashlib.md5()
    s=str.encode('utf-8')
    m.update(s)
    return m.hexdigest()


def hex_md5_wz(requestFlag, renCode_first):
    rndCode = hex_md5(hex_md5(renCode_first).upper()).upper()
    # return requestFlag, rndCode
    get_login(requestFlag, rndCode)


# 登录
def get_login(requestFlag, rndCode):
    url = "https://cg.95306.cn/proxy/passport/submit"
    headers = {
        "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        'Content-Type': 'application/json'
    }
    data = {
        "loginType": 3,
        "returnUrl": "https://cg.95306.cn/",
        "requestFlag": requestFlag,
        "userAccount": "",
        "userPassword": "4EEDC48F39B9D37FB19B9B7A5EAEC5FF",
        "rndCode": rndCode,
        "loginMedia": "Chrome: 86.0.4240.198",
        "loginDevice": "mac",
        "isWeakPwd": "0"
    }
    session = requests.Session()
    res = session.post(url=url, headers=headers, data=json.dumps(data), timeout=10, verify=False)
    login_json = json.loads(res.text)

    Authorization = login_json['msg']
    data_url = login_json['data']
    print(Authorization, data_url)
    # return Authorization
    # item={
    #     'Authorization':Authorization,
    # }
    conn.set('Authorization', Authorization)



def main():
    get_requestFlag()
    


if __name__ == "__main__":
    # ul = CgAuthorization(s)
    # ul.get_requestFlag()
    # ul.get_login()
    main()
"""
https://cg.95306.cn/proxy/passport/randInit/80404D0C6D24E87F650FF7D1985CD762
https://cg.95306.cn/proxy/passport/coordinate/v1/aa0242e8da4bd089dc294e6ced13c182
https://cg.95306.cn/proxy/passport/coordinate/v2/aa0242e8da4bd089dc294e6ced13c182
https://cg.95306.cn/proxy/passport/coordinate/v3/aa0242e8da4bd089dc294e6ced13c182
"""

"https://cg.95306.cn/weblogic1/export/file/business/upload_attachment_files/2021-02-04/1612399749271129ebbfe-c196-43ac-a8a1-12e7b0a1e2fc.rar"
