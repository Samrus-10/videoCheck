from django.shortcuts import render
from django.http import HttpResponse as Response, JsonResponse

from .models import FILE, DataMarket, STATION, AUDIO
#-----------------------------
import json
import os
import io
import random
from datetime import datetime
#-----------------------------
# Create your views here.


def giveFile(req):
    if req.method == 'POST':
        file = FILE()
        file.directions = 'Colonko_Server/static/file/'
        file.file_name = req.FILES['sendFile']
        file.file_clear_name = file.file_name.name
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

def startRecord(req):
    if req.method == 'POST':

        data_body = json.loads(req.body)

        id_station = data_body['StationId']
        id_session = random.randint(100, 999)
        allRecords = STATION.objects.in_bulk()

        if (len(allRecords.keys()) == 0):
            id_session = str(id_session) + str(1)
        else:
            lastNumber = len(allRecords.keys()) + 1
            id_session = str(id_session) + str(lastNumber)

        data = datetime.now()
        print(data)

        Obj = STATION()
        Obj.id_station = str(id_station)
        Obj.id_session = str(id_session)
        Obj.time = str(data)
        Obj.save()

    return JsonResponse({"SessionId": "{0}".format(id_session), "Answer": "Ok"})


def sendAudio(req):
    if req.method == 'POST':
        sendObj = json.loads(req.body)
        # print(sendObj['StationId'])
        # print(sendObj['AudioFile'])
        # print(sendObj['TimeStart'])
        # print(sendObj['TimeEnd'])
        # print(sendObj['SessionId'])
        data = datetime.now()

        path = 'static/file/'
        nameFile = "_audioFile.wav"
        allRecords = AUDIO.objects.in_bulk()

        if(len(allRecords.keys()) == 0):
            id = '1'
        else:
            id = str(len(allRecords.keys()) + 1)

        fullFileName = path + id + nameFile
        try:
            with open(fullFileName, mode='w+b') as f:
                f.write(bytes(sendObj['AudioFile']))
        except:

            audioObj = AUDIO()
            audioObj.id_station = str(sendObj['StationId'])
            audioObj.path_to_file = str(fullFileName)
            audioObj.id_session = str(sendObj['SessionId'])
            audioObj.time_start = str(sendObj['TimeStart'])
            audioObj.time_end = str(sendObj['TimeEnd'])
            audioObj.time = str(data)
            audioObj.save()

            return JsonResponse({"Answer": "Bad encoding"})

        audioObj = AUDIO()
        audioObj.id_station = str(sendObj['StationId'])
        audioObj.path_to_file = str(fullFileName)
        audioObj.id_session = str(sendObj['SessionId'])
        audioObj.time_start = str(sendObj['TimeStart'])
        audioObj.time_end = str(sendObj['TimeEnd'])
        audioObj.time = str(data)
        audioObj.save()

    return JsonResponse({"Answer": "Ok"})

