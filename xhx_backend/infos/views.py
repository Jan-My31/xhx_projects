from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

import datetime
from .models import Infolist,Fileslist
from .serializers import InfolistSerializer,FileslistSerializer
from .filters import InfoFilter,FileFilter



import datetime

class InfoPagination(PageNumberPagination):
    page_size =10
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 20




class InfoListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    #列表页, 分页， 搜索， 过滤， 排序
    queryset = Infolist.objects.all()
    serializer_class = InfolistSerializer
    pagination_class = InfoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class=InfoFilter
    search_fields = ('info_text', 'info_date','update_time', 'info_market','id')
    ordering_fields = ('info_date',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class InfoListNowViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # 列表页, 分页， 搜索， 过滤， 排序
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')
    queryset = Infolist.objects.filter(info_date =now_date)
    serializer_class = InfolistSerializer
    pagination_class = InfoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class=InfoFilter
    search_fields = ('info_text', 'info_date','update_time', 'info_market','id')
    ordering_fields = ('info_date',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class FileslistViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    #列表页, 分页， 搜索， 过滤， 排序
    queryset = Fileslist.objects.all()
    serializer_class = FileslistSerializer
    # pagination_class = InfoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class=FileFilter
    search_fields = ( 'uid',)
  
