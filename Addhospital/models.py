from django.db import models
class hosinfo(models.Model):
    hname=models.CharField(max_length=100)
    hregistration=models.CharField(max_length=100)
    htreatment=models.CharField(max_length=100)
    hbed=models.IntegerField()
    hpassword=models.CharField(max_length=100)
    hstate=models.CharField(max_length=100)
    hcity=models.CharField(max_length=100)
    hcontact=models.CharField(max_length=12)
    haddress=models.CharField(max_length=300)
    hapos=models.IntegerField(default=0)
    hbpos=models.IntegerField(default=0)
    hopos=models.IntegerField(default=0)
    habpos=models.IntegerField(default=0)

    haneg= models.IntegerField(default=0)
    hbneg= models.IntegerField(default=0)
    honeg = models.IntegerField(default=0)
    habneg = models.IntegerField(default=0)


    class Meta:
        db_table="hosinfo"
