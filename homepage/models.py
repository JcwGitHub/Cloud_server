# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models


class DollRoom(models.Model):
    imageUrl = models.CharField(max_length=255)
    title = models.CharField(max_length=30)
    peopleCount = models.IntegerField()
    live_rtmp_url = models.CharField(max_length=255,default="")
    user_rtmp_url = models.CharField(max_length=255,default="")
    chatroom_id = models.IntegerField(default=0)
    room_id = models.AutoField(primary_key=True)
    def __unicode__(self):
        return self.title


#商品表
class Commodity(models.Model):
    "icon"
    icon = models.FileField(upload_to = 'goods_icon')
    name = models.CharField(max_length=65)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    pass