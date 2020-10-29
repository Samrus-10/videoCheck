from django.shortcuts import render
from django.http import HttpResponse as Response
from .models import FILE, DataMarket
#-----------------------------
import json
import os
from datetime import datetime
#-----------------------------
# Create your views here.

def giveFile (req):
    if req.method == 'POST':
        file = FILE()
        file.directions = 'Colonko_Server/static/file/'
        file.file_name = req.FILES['sendFile']
        file.file_clear_name =  file.file_name.name
        #print(file.file_name.name)
        file.save()
    return Response("200(Ok)")

def makeDataMarkets(req):
    if req.method == 'POST':
        data = DataMarket()
        data.id_station = req.POST.get("id_station")
        #получаю текущую дату
        current_data = datetime.now()

        data.year = str(current_data.year)
        data.month = str(current_data.month)
        data.day = str(current_data.day)

        data.hours = str(current_data.hour)
        data.minutes = str(current_data.minute)
        data.seconds = str(current_data.second)

        data.save()

    return Response("200(Ok)")



