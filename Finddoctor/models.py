from django.db import models


class patientdoctor(models.Model):
    hname=models.CharField(max_length=100,default="0")
    hpatient=models.CharField(max_length=100,default="0")
    hdoctor=models.CharField(max_length=100,default="0")
    hdate=models.CharField(max_length=100,default="0")
    class Meta:
        db_table="patientdoctor"





