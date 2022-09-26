import imp
from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def display(request):
    return HttpResponse("<h1>hola mundo</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora actual: </b>" + str(dt)
    return HttpResponse(s)
