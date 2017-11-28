from django.http import HttpResponse


print("DataBase")
def TestDB(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.user)
    return HttpResponse("添加数据成功11")