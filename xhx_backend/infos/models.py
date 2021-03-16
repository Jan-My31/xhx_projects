from django.db import models
import django.utils.timezone as timezone

# Create your models here.
#公告列表
class Infolist(models.Model):
    id = models.CharField(verbose_name='Id',max_length=50,primary_key=True)
    info_text = models.CharField(verbose_name='公告名称',max_length=100)
    info_id = models.CharField(verbose_name='查询ID',max_length=100)
    info_type = models.CharField(verbose_name='公告类型',max_length=100)
    info_market = models.CharField(verbose_name='所属市场', max_length=100)

    info_date = models.DateField(verbose_name='发布时间',max_length=50)
    # 公告链接
    info_link = models.URLField(verbose_name='公告链接',unique=True)
    info_detail=models.TextField(verbose_name="公告详情")
    update_time=models.CharField(verbose_name='更新日期',max_length=50)
    create_time=models.CharField(verbose_name='创建时间',max_length=50 )

    class Meta:
        db_table="infos_list"
        verbose_name="公告列表"
        verbose_name_plural = verbose_name
        ordering=['-info_date']

    def __str__(self):
        return self.info_text




class Fileslist(models.Model):
    #文件id
    id = models.CharField(verbose_name='Id',max_length=50,primary_key=True)
    #uid 对应infos表中的id
    uid=models.CharField(verbose_name="uid",max_length=50)
    file_id=models.CharField(verbose_name="文件id",max_length=500)
    file_name=models.CharField(verbose_name="文件名称",max_length=500)
    info_text=models.CharField(verbose_name="公告名称",max_length=500)
    info_url=models.CharField(verbose_name="公告url",max_length=500)


    class Meta:
        db_table = "files_list"
        verbose_name_plural="文件信息"

    def __str__(self):
        return self.id
    

    