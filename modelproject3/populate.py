import os   
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings') 
import django   
django.setup()   
  
from testapp.models import Student   
from faker import Faker   
from random import randint   

fake = Faker()

def phonenumbergen():   
    d1 = randint(6, 9)   
    num = str(d1)   
    for _ in range(9):   
        num += str(randint(0, 9))   
    return int(num) 

def populate(n):   
    for _ in range(n):   
        frollno = fake.random_int(min=1, max=999)   
        fname = fake.name()   
        fdob = fake.date()   
        fmarks = fake.random_int(min=1, max=100)   
        femail = fake.email()   
        fphonenumber = phonenumbergen()   
        faddress = fake.address()   
        student_record, created = Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            email=femail,
            phonenumber=fphonenumber,
            address=faddress
        )   
n=int(input("enter the records:-"))
populate(30)
print("records entered:")
