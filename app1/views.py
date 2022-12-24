from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def laddu(request):
    return HttpResponse('<h1>laddu is so sweet</h1>')

def latha(request):
    return HttpResponse('<b>latha is very short girl</b>')

def aishu(request):
    return HttpResponse('<b><i><marquee>aishu is very cute</marquee></i></b>')

