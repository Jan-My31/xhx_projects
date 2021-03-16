#-*— coding:utf-8 -*-
# serializers.py
# 用户序列化
from rest_framework import serializers

from users.models import Userlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlist
        # 要显示出来的字段
        fields = ('id', 'u_name', 'u_password')