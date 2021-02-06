from django.shortcuts import render,redirect
from .models import hospital
import datetime
from django.http import HttpResponse
from django.db.models import Q
from django.db import connection
from faker import Faker


def search(request):

    return render(request,'search.html')

def result(request):

    if request.method=="POST":
        search = request.POST.get("sera")
        search=search.upper()
        if search:
            row=hospital.objects.raw("SELECT * FROM hospital where hcity=%s",[search])

            return render(request, 'result.html',{"sr": row})
    return render(request,"search.html")

def addmovie(request):
    now = datetime.datetime.now()
    x = hospital.objects.all()
    return render(request,"home.html",{'movies': x,"time":now})
def add_hospital(request):
    name= request.POST.get('cname','default')
    city= request.POST.get('ccity','default')
    treat=request.POST.get('ctreat','default')
    bed = request.POST.get('cbed','default')
    blood= request.POST.get('cblood','default')
    patient=request.POST.get('cpatient','default')
    name=name.upper()
    city=city.upper()
    treat=treat.upper()
    blood=blood.upper()



    movie_info=hospital(hname=name,hcity=city,htreat=treat,hblood=blood,hbed=bed,hpatient=patient)

    if request.method=='POST':

        movie_info.save()



    return render(request,"add_hospital.html")

def health_library(request):
    rong=['#FA8072','#DCA4D9','#B7A4DC','#92ABE5','#CEEFE2']
    color={"x":rong}
    return render(request,'health_library.html',color)


