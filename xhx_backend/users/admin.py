from django.contrib import admin

# Register your models here.
from users.models import Userlist


class UserlistAdmin(admin.ModelAdmin):
    # 文章中显示的字段
    list_display = ('username','password',)
    # 满15条分页
    list_per_page = 20
admin.site.register(Userlist,UserlistAdmin)

