from django.db import models
# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    empsal=models.FloatField()
    
#the django class will covert the Emloyee table .

# the table name of the dat as follows like testapp_Employee

# auto increment will given by the django server id will given by the dajngo it will auto increment by the situation.