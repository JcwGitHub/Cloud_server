#coding=utf-8
import json


class requestpmanage:
    def __init__(self,requestmsg):
        if requestmsg.user.is_authenticated():
            print ("已经登录，name:"+requestmsg.user.username)
        else:
            print ("未登录")
        self.data = requestmsg.body
        self.json = json.loads(self.data)
        self.ispost = requestmsg.method == 'POST'
        self.isget = requestmsg.method == 'GET'
        self.islogin = requestmsg.user.is_authenticated()
        self.username = requestmsg.user.username
    pass

    def getvalue(self,key):
        return self.json[key]
