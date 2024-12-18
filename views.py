from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import *

#importing thr form
#from MyProject import loginform
#create your views here

from django.http import HttpResponse ,HttpResponseNotFound
from django.views.decorators.http import require_http_methods 
@require_http_methods(["GET"])
def hello(request):
    return HttpResponse("<h1>Hello, Welcome to Django</h1>")

def greetings(request, msg="Good morning"):
    message="<h1>Hello, welcome to django!</h1><Br>"+msg
    return HttpResponse(message)
def members(request):
    template=loader.get_template('training.html')
    return HttpResponse(template.render())