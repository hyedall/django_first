# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world.')

def some_url(request):
    return HttpResponse('Some url을 구현해봤습니다.')