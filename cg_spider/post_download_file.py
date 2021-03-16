#-*— coding:utf-8 -*-
import requests
import json

def download_file():
    headers={
    "Cookie": "JSESSIONID=-CG4KEsakDs23cRypz7xdDSGmwRDvhY_yS-g54FM7Se2IQupqNnC!-1236011016"
    }
    data={
        "id":"OQ002021020963367695",
        "fileID":"OQ002021020963367256",
        "flagForward":"1",
        # "fileID0":"OQ002021020963367256"
        
    }

    url="http://wz.guangzh.95306.cn/downloadfile.do?flag=1"

    response=requests.post(url,headers=headers,data=data)
    print(response.text)
    with open('2.rar', "wb") as code:
        # print("%s已经下载"%file_name)
        code.write(response.content)

def main():
    download_file()

if __name__ =="__main__":
    main()