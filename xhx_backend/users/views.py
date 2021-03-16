from django.shortcuts import render

# Create your views here.

import time
from users import models
from django.http import JsonResponse
from rest_framework.views import APIView


class AuthView(APIView):

    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':'登录成功'}
        try:
            # 参数是datadict 形式
            usr = request.data.get('username')
            pas = request.data.get('password')

            # usr = request._request.POST.get('username')
            # pas = request._request.POST.get('password')

            # usr = request.POST.get('username')
            # pas = request.POST.get('password')

            print(usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = models.Userlist.objects.filter(username=usr,password=pas).first()
            print(obj)
            print(type(obj))
            print(obj.username)
            print(obj.password)
            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = str(time.time()) + usr
            print(token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            #ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)