#-*— coding:utf-8 -*-


from users.views import AuthView
from django.urls import path, re_path

urlpatterns = [
    # path('token/',obtain_jwt_token),
    # path('getToken/', views.getToken, name='getToken'),
    path('users/', AuthView.as_view()),
    re_path('users/(?P<pk>\d+)/', AuthView.as_view(),name='user-detail'),

]
