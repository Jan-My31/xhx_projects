"""xhx_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from infos.views import InfoListViewSet,InfoListNowViewSet,FileslistViewSet
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
# from users.views import UsersAPIView

admin.site.site_title='销售公告管理系统'
admin.site.site_header = '销售公告管理系统'
router = DefaultRouter()
router.register(r'allinfo', InfoListViewSet,basename='allinfo')
router.register(r'info',InfoListNowViewSet,basename='info')
router.register(r'files',FileslistViewSet,basename='files')

# router.register(r'markets',views.MarketsNowViewSet,basename='markets')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('up/',include('users.urls')),

    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
  
]


# 
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    
