import requests
from lxml import etree

def get_detail():
    headers={
        "Cookie": "JSESSIONID=-CG4KEsakDs23cRypz7xdDSGmwRDvhY_yS-g54FM7Se2IQupqNnC!-1236011016"
    }

    url="http://wz.guangzh.95306.cn/mainPageNotice.do?method=info&id=OQ002021020462968560%40OQ002021020462968251%4030"
    response=requests.get(url,headers=headers,verify=False)
    # res=etree.HTML(response.text)
    print(response.text)


def main():
    get_detail()



if __name__=="__main__":
    main()

    