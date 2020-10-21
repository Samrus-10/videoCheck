from django.shortcuts import render
from django.http import HttpResponse as Response
from .models import FILE
import json
import os
# Create your views here.

def some(req):
    return Response('It works')


def giveFile (req):
    if req.method == 'POST':
        file = FILE()
        file.directions = 'Colonko_Server/static/file/'
        file.file_name = req.FILES['sendFile']
        file.save()


