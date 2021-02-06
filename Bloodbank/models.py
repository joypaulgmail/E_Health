from django.db import models
class bloodpatient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    blood=models.CharField(max_length=100)
    medical=models.CharField(max_length=150)
    number=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    class Meta:
        db_table="bloodpatient"

class bloodbank(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    blood=models.CharField(max_length=100)
    medical=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    class Meta:
        db_table="bloodbank"
        



