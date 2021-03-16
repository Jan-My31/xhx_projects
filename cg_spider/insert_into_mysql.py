#-*— coding:utf-8 -*-
import pymysql
class MysqlPipeline(object):
    try:
        def __init__(self):
            # self.conn=pymysql.connect("127.0.0.1","root","xhx_projects")
            self.conn =pymysql.connect(database="", user="xhx", password="Xhx121314.", host="",
                                         port=3306)
       
            self.cursor = self.conn.cursor()

        def process_item(self, item):
            insert_sql = "insert into infos_list( id,info_text,info_id,info_type,info_date,info_link,update_time,create_time,info_detail) VALUES (%(id)s,%(info_text)s,%(info_id)s,%(info_type)s,%(info_date)s,%(info_link)s,%(update_time)s,%(create_time)s,%(info_detail)s)"

            self.cursor.execute(insert_sql, item)
            self.conn.commit()
        def file_process_item(self,item):
            insert_sql = "insert into files_list(id,uid,info_text,info_url,file_id,file_name) VALUES (%(id)s,%(uid)s,%(info_text)s,%(info_url)s,%(file_id)s,%(file_name)s)"

            self.cursor.execute(insert_sql, item)
            self.conn.commit()

        def close(self):
            self.cursor.close()
            self.conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    mysql_con = MysqlPipeline()
    print(mysql_con)
