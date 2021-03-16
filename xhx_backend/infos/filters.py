#-*— coding:utf-8 -*-

import django_filters

from .models import Infolist,Fileslist


class InfoFilter(django_filters.rest_framework.FilterSet):
    id =django_filters.CharFilter(field_name='id',lookup_expr='icontains')
  
    info_market = django_filters.CharFilter(field_name='info_market', lookup_expr='icontains')
    update_time = django_filters.CharFilter(field_name='update_time', lookup_expr='icontains')

    class Meta:
        model =Infolist
        fields = ['id','info_market','update_time']
        
        
class FileFilter(django_filters.rest_framework.FilterSet):
    uid = django_filters.CharFilter(field_name='uid', lookup_expr='icontains')

    class Meta:
        model = Fileslist
        fields = ['uid']
    