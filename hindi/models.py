from django.db import models
class hospital(models.Model):
    hname=models.CharField(max_length=100)
    hcity=models.CharField(max_length=100)
    htreat=models.CharField(max_length=100)
    hbed=models.IntegerField()
    hblood=models.CharField(max_length=100)
    hpatient=models.IntegerField()

    class Meta:
        db_table="hospital"








