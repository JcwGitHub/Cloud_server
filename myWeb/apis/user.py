#coding=utf-8
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse

from myWeb.apis import goods
from myWeb.apis.localdefine import gusername,gpassword,gresponcache
from myWeb.utils.requestmanage import requestpmanage

from django.shortcuts import render

def auth_test(request):
    return render(request, "Html1.html")


def auth_createaccount(request):
    _rm = requestpmanage(request)
    if _rm.ispost:

        #检查用户名重复
        _count = User.objects.filter(username=_rm.getvalue(gusername)).count()

        if _count>0:
            return HttpResponse("已经存在")
        else:
            _user = User.objects.create_user(_rm.getvalue(gusername),
                                            'None',_rm.getvalue(gpassword))
            if _user:
                return HttpResponse("创建成功")
    return gresponcache.error()


def auth_changepassword(request):
    _rm = requestpmanage(request)
    if _rm.ispost and _rm.islogin:
        _oldpassword = _rm.getvalue('oldpassword')
        _newpassword = _rm.getvalue('newpassword')
        _user = auth.authenticate(username=_rm.username, password=_oldpassword)
        if _user:
            _user.set_password(_newpassword)
            _user.save()
            return HttpResponse("changepassword success")
        return HttpResponse("changepassword notvalid")
    else:
        return gresponcache.loginonfirst()
    return gresponcache.error()



def auth_login(request):
    _rm = requestpmanage(request)
    if _rm.islogin:
        return HttpResponse("alredy login")
    if _rm.ispost:
        # 校验用户
        _user = auth.authenticate(username=_rm.getvalue(gusername), password=_rm.getvalue(gpassword))
        #校验成功  用户需要存在并且激活状态
        if _user is not None and _user.is_active:
            auth.login(request,_user)
            return HttpResponse("login success")
        else:
            return HttpResponse("login faild")
    return gresponcache.error()



def auth_logout(request):
    auth.logout(request)
    return HttpResponse("退出登录")


def auth_changeheadimage(request):

    return HttpResponse("ok")