from django.shortcuts import render
from django.http import HttpResponse
#create your views here

def  disp(request):
    s = "<h1>Hello student this the my first web response</h1>"
    return HttpResponse(s)
