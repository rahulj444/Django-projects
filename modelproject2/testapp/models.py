from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    e_name=models.CharField(max_length=30)
    e_sal=models.FloatField()
    e_addr=models.CharField(max_length=30)
    e_number=models.IntegerField()
