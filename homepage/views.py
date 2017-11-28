# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from homepage import models

#获取首页数据
def getList(request):
    page = request.GET['page']
    froms = (int(page) - 1) * 10
    to = froms + 10
    json = serializers.serialize("json",models.DollRoom.objects.all()[froms:to])
    return HttpResponse(str(json))