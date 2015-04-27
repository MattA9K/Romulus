# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")

def html(request):
    return render_to_response('home.html')