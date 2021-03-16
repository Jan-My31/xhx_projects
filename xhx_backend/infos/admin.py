from django.contrib import admin
from .models import  Infolist

# Register your models here.

class InfosAdmin(admin.ModelAdmin):

    #文章中显示的字段
    list_display = ('info_text','info_id','info_market','info_type','info_date')
    #满15条分页
    list_per_page = 20

    #
    list_filter = ('info_market','info_date',)
    #后台数据排列方式
    ordering =('-info_date',)
    
    date_hierarchy ='info_date'

admin.site.register(Infolist,InfosAdmin)

