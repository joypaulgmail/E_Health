from django.shortcuts import render
from .models import doctor
from Doctor.models import doctorappoient
from django.db.models import Q
import datetime
import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def doctoradd(request):
    return render(request,"DOCTOR/doctoradd.html")
def doctoretail(request):
    if request.method=="POST":
        name = request.POST.get("name").upper()
        registration=request.POST.get("registration").upper()
        qualification=request.POST.get("qualification").upper()
        speciality=request.POST.get("speciality").upper()
        contact=request.POST.get("contact").upper()
        state=request.POST.get("state").upper()
        city=request.POST.get("city").upper()
        address=request.POST.get("clinic").upper()
        experience=request.POST.get("experience").upper()
        fees=request.POST.get("fees").upper()
        picture=request.FILES["photo"]

        doc=doctor(name=name,registration=registration,qualification=qualification,speciality=speciality,contact=contact,state=state,
                   city=city,	address=address,experience=experience,	fees=fees,	photo=picture)

        doc.save()




    return render(request,"DOCTOR/doctorsearch.html")

def doctorsearch(request):
    return render(request,"DOCTOR/doctorsearch.html")

def doctorsearchsubmit(request):

    if request.method == "POST":
        location = request.POST.get("location").upper()
        speciality= request.POST.get("speciality").upper()

        if location and speciality:
            seens =doctor.objects.raw("select * from doctor  WHERE city = %s and speciality=%s", [location,speciality])

    return render(request, "DOCTOR/doctorsearch.html",{"details":seens})

def doctorapoint(request):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")

    now = now.strftime("%Y-%m-%d %H:%M:%S")

    if request.method == "POST":
        name=request.POST.get("name").upper()
        regis= request.POST.get("regis").upper()
        if regis and name:
            query=doctor.objects.get(registration=regis)
            number=query.contact
            st=query.name

            '''
            to send way 2 sms
               response = sendPostRequest(URL, '3388HNL62ZHAR5ZC30KTEDKRLAJ61N74', 'SI1FC0Y6NAYF0NQL', 'stage',number,
                                       'sudhar', name+' send you Appointment request..Thank You')
            '''

            sv=doctorappoient(name=st,registration=regis,pattient=name,date=now)
            sv.save()











    return render(request, "DOCTOR/doctorsearch.html")


