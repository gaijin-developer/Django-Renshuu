from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

articles={"sports":"sports page","finance":"finance page"}

def news_view(request,topic):
   return HttpResponse(topic)
# def finance_view(request):
#    return HttpResponse(articles["finance"])

def add_view(request,num1,num2):
    result = num1 + num2
    return HttpResponse(str(result))