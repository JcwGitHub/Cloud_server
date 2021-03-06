#coding:utf-8

from myWeb.utils.requestmanage import requestpmanage
from myWeb.apis.localdefine import gresponcache
from homepage.models import Commodity

from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize


import os
from myWeb.settings import STATIC_GOODS_ICON


def goodslist(request):
    _rm = requestpmanage(request)
    if  _rm.ispost:
        _startid = (_rm.getvalue('page')-1)*10
        if _startid>Commodity.objects.count():
            return JsonResponse({"type":"error"})
        _end = _startid+9
        _goods = serialize('json',Commodity.objects.all()[_startid:_end])
        return JsonResponse(_goods,safe=False)
    return gresponcache.error()


def goodsicon(request):
    _rm = requestpmanage(request)
    if _rm.ispost:
        goodsid = _rm.getvalue('goodsid')
        goodsname = str(goodsid)+".png"
        imagepath = os.path.join(STATIC_GOODS_ICON, goodsname)
        if os.path.exists(imagepath):
            print(imagepath)
            image_data = open(imagepath, "rb").read()
            return HttpResponse(image_data, content_type="image/jpg")
        else:
            return gresponcache.error()
