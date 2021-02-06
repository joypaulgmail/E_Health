from django.db import models
class doctor(models.Model):
    name=models.CharField(max_length=100,default="0")
    registration=models.CharField(max_length=100,default="0")
    qualification=models.CharField(max_length=100,default="0")
    speciality=models.CharField(max_length=100,default="0")
    contact= models.CharField(max_length=100, default="0")
    state = models.CharField(max_length=100, default="0")
    city = models.CharField(max_length=100, default="0")
    address = models.CharField(max_length=100, default="0")
    experience= models.CharField(max_length=100, default="0")
    fees=models.IntegerField()
    photo=models.FileField(upload_to='media/',blank=True)
    class Meta:
        db_table="doctor"

class doctorappoient(models.Model):
    name=models.CharField(max_length=100,default="0")
    registration=models.CharField(max_length=100,default="0")
    pattient=models.CharField(max_length=100,default="0")
    date=models.CharField(max_length=100,default="0")
    class Meta:
        db_table="doctorappoient"









