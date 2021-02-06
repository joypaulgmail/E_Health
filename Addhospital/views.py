from django.shortcuts import render
from .models import hosinfo
from Finddoctor.models import patientdoctor
from django.db.models import Q
from django.db import connection
def addhospital(request):
    return render(request,'ADDHOSPITAL/add_hospital.html')
def hospitalsubmit(request):
    name= request.POST.get('name','default').upper()
    registration= request.POST.get('registration','default').upper()
    treatment= request.POST.get('treatment','default').upper()
    bed= request.POST.get('bed','default').upper()
    password= request.POST.get('password','default').upper()
    state= request.POST.get('state','default').upper()
    city= request.POST.get('city','default').upper()
    contact= request.POST.get('contact','default').upper()
    address= request.POST.get('address','default').upper()

    hospital_info=hosinfo(hname=name,hregistration=registration,htreatment=treatment,hbed=bed,hpassword=password,hstate=state,hcity=city,hcontact=contact,haddress=address)
    patient=patientdoctor(hname=name)



    if request.method=='POST':
        hospital_info.save()
        patient.save()



    return render(request,'ADDHOSPITAL/login.html')

def bloodsubmit(request):
    if request.method=="POST":
        register = request.POST.get('register', 'default').upper()
        password = request.POST.get('password', 'default').upper()
        apos = request.POST.get('A+', 'default').upper()
        bpos = request.POST.get('B+', 'default').upper()
        opos = request.POST.get('O+', 'default').upper()
        abpos = request.POST.get('AB+', 'default').upper()
        aneg = request.POST.get('A-', 'default').upper()
        bneg = request.POST.get('B-', 'default').upper()
        oneg = request.POST.get('O-', 'default').upper()
        abneg = request.POST.get('AB-', 'default').upper()
        regis= hosinfo.objects.raw("SELECT * FROM hosinfo where hregistration=%s and hpassword=%s", [register,password])
        if regis:
            obj=hosinfo.objects.get(hregistration=register)
            obj.hapos=apos
            obj.hbpos=bpos
            obj.hopos=opos
            obj.habpos =abpos
            obj.haneg=aneg
            obj.hbneg=bneg
            obj.honeg=oneg
            obj.habneg=abneg


            if request.method=="POST":
                obj.save()


                return render(request, 'ADDHOSPITAL/successful.html',{"name":obj})
        return render(request,'ADDHOSPITAL/login.html')








