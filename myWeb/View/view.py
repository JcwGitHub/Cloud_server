from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'HelloWorld!'
    return render(request, 'Html1.html', context)