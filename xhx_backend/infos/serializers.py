#-*— coding:utf-8 -*-
from .models import Infolist,Fileslist
from rest_framework import serializers



class InfolistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Infolist
      
        fields="__all__"

class FileslistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fileslist
        fields="__all__"
