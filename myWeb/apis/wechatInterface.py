import hashlib

from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
WEIXIN_TOKEN = 'jcwjcwjcw'

@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
    	print("23123131")
        if tmp_str == signature:
            print("23123131")
            return HttpResponse(echostr)
        else:
            print("error")
            return HttpResponse("weixin  index")
    else:
        xml_str = smart_str(request.body)
        print(xml_str)
        return render(request, "templates.Html1.html")