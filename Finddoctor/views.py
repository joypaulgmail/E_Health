from django.shortcuts import render
from Addhospital.models import hosinfo
from Finddoctor.models import patientdoctor
from django.db.models import Q
import datetime
now = datetime.datetime.now()
time=now.strftime("%H:%M:%S")

now=now.strftime("%Y-%m-%d %H:%M:%S")
def finddoctor(request):
    if request.method=="POST":
        search = request.POST.get("city")
        search=search.upper()

        if search:
            q = None
            for word in search.split():

                q_aux = Q(hname__icontains=word) | Q(hcity__icontains=word)
            q = q_aux
            seens = hosinfo.objects.filter(q)


            return render(request,'FINDDOCTOR/find_doctor.html',{"name":seens})


        return render(request,"search.html")


def adddoctor(request):
    return render(request,'FINDDOCTOR/add_doctor.html')




def bedbook(request):
    search = request.POST.get("id").upper()
    name=request.POST.get("name").upper()
    blood = request.POST.get("blood").upper()
    patientname=patientdoctor(hname=search,hpatient=name,hdate=now)
    p=hosinfo.objects.get(hname=search)
    if blood=="A+":
        p.hapos = p.hapos - 1
    elif blood=="B+":
        p.hbpos = p.hbpos - 1
    elif blood=="O+":
        p.hopos = p.hopos - 1
    elif blood=="AB+":
        p.habpos =  p.habpos-1
    elif blood=="A-":
        p.haneg = p.haneg-1
    elif blood=="B-":
        p.hbneg = p.hbneg-1
    elif blood=="O-":
        p.honeg = p.honeg-1
    elif blood=="AB-":
        p.habneg = p.habneg-1

    p.hbed=p.hbed-1
    if p.hbed>1:
        if request.method=='POST':
            p.save()
            patientname.save()
            return render(request, "FINDDOCTOR/bed_book.html",{"time":time})
    return render(request,"FINDDOCTOR/finddoctor.html")





