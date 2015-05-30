# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.


def test(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")

def index(request):
    return render_to_response('index.html')


def json(request):

    json = {"test":"hello"}
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")