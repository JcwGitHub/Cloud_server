#coding=utf-8
from django.http import HttpResponse


gusername = 'username'
gpassword = 'password'

# _rm = requestpmanage(request)
# if _rm.ispost and _rm.islogin:
#     pass
# else:
#     return responcache.loginonfirst()



class responcache:
    def loginonfirst(self):
        return HttpResponse("login on first")

    def error(self):
        return HttpResponse("error")

gresponcache = responcache()



