from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('It Works')
