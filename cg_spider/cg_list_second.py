# -*— coding:utf-8 -*-
# -*— coding:utf-8 -*-

import requests

requests.packages.urllib3.disable_warnings()
import time
from insert_into_mysql import MysqlPipeline
import json
from lxml import etree
import os
import uuid
from redis import Redis
import pymysql

# print(type(authorization), authorization)

# Authorization=get_requestFlag()
# print(Authorization)
basepath = "/www/wwwroot/xhx_projects/xhx_backend/"

def get_content():
    conn = pymysql.connect(database="xhx_projects", user="xhx", password="Xhx121314.", host="45.15.10.32",
                           port=3306)
    cursor = conn.cursor()
    cursor.execute(r'SELECT id,info_text,info_link from infos_list where info_market="中国铁路沈阳局集团有限公司"')
    all_content = cursor.fetchall()
    return all_content


def get_file(info_text, id, info_url):
    headers = {
        "Cookie": "JSESSIONID=8X33_usP5vakaSCF_wwpM7gnLV7NbX2sqdd3tayb6zL-aOi9biow!-1298108568",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",

    }
    file_res = requests.get(info_url, headers=headers, verify=False, timeout=5)
    # print(file_res.text)
    files = etree.HTML(file_res.text)
    files_id = files.xpath('//input[starts-with(@id,"fileID")]/@value')
    url_id = info_url[-48:-28]
    files_name=files.xpath('//a[starts-with(@href,"javascript:downLoad")]/text()')


    files_dict=dict(zip(files_id,files_name))
    print(type(files_dict),files_dict)
    file_items = []
    for file_id in files_id:
        file_name=files_dict[file_id]

        download_file(file_name, file_id, id,url_id,info_url)

        file_item = {
            "id": str(uuid.uuid1()).replace("-", ''),
            "uid": id,
            "info_text": info_text,
            "info_url": info_url,
            "file_id": file_id,
            "file_name": file_name

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

        # data = {
        #     "id": url_id,
        #     "fileID": file_id,
        #     "flagForward": "1",
        #
        # }


#     if "forwardList" in file_json['data']:
#         for forward in file_json['data']['forwardList']:
#             file_id = forward["id"]
#             file_name = forward["filename"]
#
#             download_file(file_name, file_id, id)
#             file_item = {
#                 "id": str(uuid.uuid1()).replace("-", ''),
#                 "uid": id,
#                 "info_text": info_text,
#                 "info_url": info_url,
#                 "file_id": file_id,
#                 "file_name": file_name
#
#             }
#             file_items.append(file_item)
#     try:
#         my = MysqlPipeline()
#
#         for item in file_items:
#             print(item)
#             my.file_process_item(item)
#         my.close()
#         print("数据存储完成")
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         # 删除已经查询到的企业id 信息
#     except Exception as e:
#
#         print(e)
#
#
def download_file(file_name, file_id, id,url_id,info_url):
    print(file_name,file_id,id,url_id)
    headers = {
        # "Cookie": "JSESSIONID=5-65ALPy1dYEu-CEgITRp7ZAVMGWhwXudAZW85CSzsV4vxsFbJ_r!338545311; security_session_verify=943a757a601709092f385b622bd7eca6",
        # "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        # 'Authorization': authorization,
        "Cookie":"JSESSIONID=8X33_usP5vakaSCF_wwpM7gnLV7NbX2sqdd3tayb6zL-aOi9biow!-1298108568",
    }

    base_url=info_url[:-81]
    url = base_url+"downloadfile.do?flag=1"
    data = {
        "id": url_id,
        "fileID": file_id,
        "flagForward": "1",


    }
    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    down_path = os.path.join(basepath, "media", id)
    if not os.path.isdir(down_path):
        os.makedirs(down_path)

    with open(os.path.join(down_path, file_name), "wb") as code:
        print("%s已经下载" % file_name)
        code.write(response.content)


#
#
#
#
#
# def get_detail(info_text, id, info_type, info_date, info_link, update_time, info_url):
#     # try
#     headers = {
#         "cookie": "AlteonPcgmh=0a03b7f31103323d1f41; st=0548ceed117a86720b01381b66731368; cgptmhCookie=mh_uanezrupe7czy2suv3crfc9yl492ih9g681d",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#         "X-Requested-With": "XMLHttpRequest",
#         'Content-Type': 'application/json',
#         'Authorization': authorization,
#
#     }
#     detail_res = requests.get(info_url, headers=headers, verify=False, timeout=5)
#     detail_json = json.loads(detail_res.text)
#     info_detail = detail_json['data']['noticeContent']['notCont']
#     info_id = detail_json['data']['noticeContent']['inforCode']
#     create_time = detail_json['data']['noticeContent']['checkTime']
#
#     # for forward in detail_json['data']['forwardList']:
#     #     file_id = forward["id"]
#     #     file_name = forward["filename"]
#     #
#     #     file_id_list.append(file_id)
#     #     file_name_list.append(file_name)
#     #     print(file_name_list,info_id)
#     item = {
#         'id': id,
#         'info_text': info_text,
#         'info_id': info_id,
#         'info_type': info_type,
#         'info_date': info_date,
#         'info_link': info_link,
#         'update_time': update_time,
#         'create_time': create_time,
#         'info_detail': info_detail,
#     }
#
#     try:
#         my = MysqlPipeline()
#
#         my.process_item(item)
#         my.close()
#         print("数据存储完成")
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         # 删除已经查询到的企业id 信息
#     except Exception as e:
#
#         print(e)


def main():
    all_content = get_content()
    for content in all_content:
        id = content[0]
        info_text = content[1]
        info_url = content[2]
        print(id, info_text, info_url)
        get_file(info_text, id, info_url)


if __name__ == '__main__':
    main()



# {'IW002021021901245980': '竞价销售文件.rar', 'IW002021021901245983': '附件2-报废物资投标函.rar', 'IW002021021901245974': '报名表.rar', 'IW002021021901245976': '附件3-报废物资授权委托书.rar'}