from django.shortcuts import render
from .models import bloodpatient
from .models import bloodbank
def blood_required(request):
    name="joy"
    return render(request,'BLOODBANK/register.html',{"name":name})

def bloodrequired_submit(request):
    if request.method=="POST":
        name=request.POST.get('name','default').upper()
        age=request.POST.get('age','default').upper()
        blood=request.POST.get('blood','default').upper()
        medical=request.POST.get('medical','default').upper()
        number=request.POST.get('number','default').upper()
        state=request.POST.get('state','default').upper()
        city=request.POST.get('city','default').upper()
        address=request.POST.get('address','default').upper()
        bloodrequired=bloodpatient(name=name,age=age,blood=blood,medical=medical,number=number,state=state,city=city,address=address)
        bloodrequired.save()

    return render(request, 'BLOODBANK/blood_required_submit.html')

def blood_donate(request):
    return render(request,'BLOODBANK/blood_donate.html')

def blood_donate_submit(request):
    if request.method == "POST":
        name = request.POST.get('name', 'default').upper()
        age = request.POST.get('age', 'default').upper()
        blood = request.POST.get('blood', 'default').upper()
        medical = request.POST.get('medical', 'default').upper()
        number = request.POST.get('number', 'default').upper()
        state = request.POST.get('state', 'default').upper()
        city = request.POST.get('city', 'default').upper()
        address = request.POST.get('address', 'default').upper()
        blood=bloodbank(name=name,age=age,blood=blood,medical=medical,number=number,state=state,city=city,address=address)
        blood.save()
    return render(request, 'BLOODBANK/blood_donate_submit.html')
