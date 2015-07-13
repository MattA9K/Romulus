# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Romulus.models import *
# Create your views here.


def test(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")

def index(request):
    hit = PageHit(remote_address=request.META['REMOTE_ADDR'], user_agent=request.META['HTTP_USER_AGENT'], referer=request.META['HTTP_REFERER'])
    hit.save()
    return render_to_response('index.html')

def json(request):
    json = {"test":"hello"}
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")

def authorize_access(request):
    return render_to_response('auth.html')