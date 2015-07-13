# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Romulus.models import *
# Create your views here.


def test(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")


def index(request):
    hit = PageHit()
    try:
        hit.remote_address=request.META['REMOTE_ADDR']
    except:
        hit.remote_address='x'

    try:
        hit.user_agent=request.META['HTTP_USER_AGENT']
    except:
        hit.user_agent='x'

    try:
        hit.referer=request.META['HTTP_REFERER']
    except:
        hit.referer='x'
    hit.save()
    return render_to_response('index.html')


def json(request):
    json = {"test":"hello"}
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")


def authorize_access(request):
    return render_to_response('auth.html')