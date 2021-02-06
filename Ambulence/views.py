from django.shortcuts import render

import socket
import requests
import geocoder

from phonenumbers import geocoder


def sendrequest(request):
    return render(request,'AMBULENCE/sendrequest.html')

def sendcordinate(request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    lati=1
    long=2









    return render(request, 'AMBULENCE/sendrequest.html',{"long":long,"lati":lati})


def sendlocation(request):
    mapboxgl = 'pk.eyJ1Ijoiam95cGF1bCIsImEiOiJjazk1OWpkNmwwMzAyM2dvbGR6Ym44OGVkIn0.-YWzjJlSHRdl32NUMQpRWQ'
    return render(request, 'AMBULENCE/location.html',{"mapbox":mapboxgl})

