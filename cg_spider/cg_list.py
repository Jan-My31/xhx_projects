# -*— coding:utf-8 -*-

import requests

requests.packages.urllib3.disable_warnings()
import time
from insert_into_mysql import MysqlPipeline
import json
import os
import uuid
from redis import Redis

conn = Redis(host='45.15.10.32', encoding='utf-8', port=6388,password='Xhx121314.')
authorization = conn.get('Authorization')

authorization=str(authorization,encoding="utf-8")
print(type(authorization),authorization)


# Authorization=get_requestFlag()
# print(Authorization)
basepath = "/www/wwwroot/xhx_projects/xhx_backend/"

def get_list():
    headers = {
        "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        'Content-Type': 'application/json'
    }
    # for pageNum in range(10,12):
    #     url = "https://cg.95306.cn/proxy/portal/elasticSearch/queryDataToEs?projBidType=02&bidType=10&noticeType=01&pageNum=%s"%pageNum
    url = "https://cg.95306.cn/proxy/portal/elasticSearch/queryDataToEs?projBidType=02&bidType=10&noticeType=01&pageNum=1"
    res = requests.get(url, headers=headers, verify=False, timeout=5)
    list_json = json.loads(res.text)

    info_list = list_json['data']['resultData']['result']
    for info in info_list:
        # print(info)
        info_text = info['notTitle'],
        # print(type(info_text), info_text)
        id = str(info['id']),
        info_type = info['noticeTypeName'],
        info_date = info['checkTime'],
        info_link = "https://cg.95306.cn/baseinfor/notice/informationShow?id=" + str(list(id)[0]),
        update_time = str(list(info_date)[0]),
        base_url = 'https://cg.95306.cn/proxy/portal/elasticSearch/indexView?noticeId='
        info_url = base_url + str(list(id)[0])

        ex=conn.sadd('info_link',info_link)

        
        if ex==1:
            print("该url没有被爬取过,可以进行数据爬取")
            get_detail(info_text,id,info_type,info_date,info_link,update_time,info_url)
            get_file(info_text,id,info_url)
        else:
            print("数据没有进行更新，没有数据抓取")

def get_file(info_text,id,info_url):
    headers = {
        "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        'Content-Type': 'application/json',
        'Authorization':authorization,

    }
    file_res = requests.get(info_url, headers=headers, verify=False, timeout=5)
    file_json = json.loads(file_res.text)
    file_items = []
    if "forwardList" in file_json['data']:
        for forward in file_json['data']['forwardList']:
            file_id = forward["id"]
            file_name = forward["filename"]

            download_file(file_name, file_id,id)
            file_item={
                "id":str(uuid.uuid1()).replace("-",''),
                "uid":id,
                "info_text":info_text,
                "info_url":info_url,
                "file_id":file_id,
                "file_name":file_name

            }
            file_items.append(file_item)
    try:
        my = MysqlPipeline()

        for item in file_items:
            print(item)
            my.file_process_item(item)
        my.close()
        print("数据存储完成")
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        # 删除已经查询到的企业id 信息
    except Exception as e:

        print(e)

def download_file(file_name,file_id,id):
    headers = {
        # "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        'Authorization': authorization,

    }
    url = "https://cg.95306.cn/proxy/portal/forwardFile/downloadFileForMainPage?fileId=%s"%str(file_id)
    print(url)
    response = requests.get(url, headers=headers)

    down_path = os.path.join(basepath,"media", list(id)[0])
    if not os.path.isdir(down_path):
         os.makedirs(down_path)

    with open(os.path.join(down_path, file_name), "wb") as code:
        print("%s已经下载"%file_name)
        code.write(response.content)





def get_detail(info_text,id,info_type,info_date,info_link,update_time,info_url):
    # try
    headers = {
        "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        'Content-Type': 'application/json',
        'Authorization': authorization,

    }
    detail_res = requests.get(info_url, headers=headers, verify=False, timeout=5)
    detail_json = json.loads(detail_res.text)
    info_detail = detail_json['data']['noticeContent']['notCont']
    info_id = detail_json['data']['noticeContent']['inforCode']
    create_time = detail_json['data']['noticeContent']['checkTime']

        # for forward in detail_json['data']['forwardList']:
        #     file_id = forward["id"]
        #     file_name = forward["filename"]
        #
        #     file_id_list.append(file_id)
        #     file_name_list.append(file_name)
        #     print(file_name_list,info_id)
    item = {
        'id': id,
        'info_text': info_text,
        'info_id': info_id,
        'info_type': info_type,
        'info_date': info_date,
        'info_link': info_link,
        'update_time': update_time,
        'create_time': create_time,
        'info_detail': info_detail,
        }

    try:
        my = MysqlPipeline()


        my.process_item(item)
        my.close()
        print("数据存储完成")
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        # 删除已经查询到的企业id 信息
    except Exception as e:

        print(e)


def main():
    get_list()



if __name__ == '__main__':
    main()
