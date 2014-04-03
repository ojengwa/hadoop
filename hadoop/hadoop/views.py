from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import urllib2

@login_required
def index(request):
    response = urllib2.urlopen('http://114.212.81.5:50070/dfshealth.jsp')
    html = response.read()
    # return html
    # return render_to_response('hello.html')
    return HttpResponse(html)

@login_required
def hello(request):
    return render_to_response('hello.html')