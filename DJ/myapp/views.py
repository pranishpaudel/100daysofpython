from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_POST,require_GET
# Create your views here.


def projects(request):
    return HttpResponse(f"Here are our projects")



def project(request,pk):
    return HttpResponse('SINGLE PROJECT'+' '+str(pk))