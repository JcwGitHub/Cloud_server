#coding=utf-8
"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from .apis import user,goods,wechatInterface
from  homepage import views as HomeView



urlpatterns = [
#test
    url(r'^$', user.auth_test),

#UserInfo
    url(r'^auth/changepassword', user.auth_changepassword),
    url(r'^auth/createaccount', user.auth_createaccount),
    url(r'^auth/logout', user.auth_logout),
    url(r'^auth/login',user.auth_login),
    url(r'^auth/updateheadimage', user.auth_changeheadimage),
#goods
    url(r'^getDollList', HomeView.getList, name='getList'),
    url(r'^goods/list',goods.goodslist),
    url(r'^goods/icon', goods.goodsicon),

#controll
    url(r'^admin/', admin.site.urls),






#wechat
    url(r'^wechat/',wechatInterface.weixin_main),
]