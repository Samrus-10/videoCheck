from django.shortcuts import render
from django.http import HttpResponse as Response

# Create your views here.

def some(req):
    return Response('It works')


