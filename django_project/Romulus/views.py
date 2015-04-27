# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")
