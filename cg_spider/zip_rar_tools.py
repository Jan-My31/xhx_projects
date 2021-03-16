#-*— coding:utf-8 -*-
from unrar import rarfile

filename="/www/wwwroot/xhx_projects/xhx_backend/media/054cf528-1e42-46c5-9ff2-79ab40f76226/TWJ202105、公告附件.rar"
rar =rarfile.RarFile(filename)

print(rar.namelist())

rar.printdir()
info=rar.infolist()
for f in info:
    print(f.filename,f.file_size,f.date_time)

rar.extractall()
# rar=rarfile.RarFile(filename, mode='r') # mode的值只能为'r'


#
# if __name__ =="__main__":
#     main()
