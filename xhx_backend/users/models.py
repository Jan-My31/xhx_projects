from django.db import models

# Create your models here.
# models.py
from django.db import models


# Create your models here.

class Userlist(models.Model):
    username = models.CharField(max_length=32,unique=True,verbose_name='用户')
    password = models.CharField(max_length=32,verbose_name='登录密码')

    class Meta:
        db_table = 'user_list'
        verbose_name = verbose_name_plural = '用户信息表'

class userToken(models.Model):
    username = models.OneToOneField(to='Userlist',on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table =  'user_token'
        verbose_name = verbose_name_plural = '用户token表'