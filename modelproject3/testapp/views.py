from django.shortcuts import render   
from testapp.models import Student   
def home_page_view(request):   
    students=Student.objects.all()   
   #students=Student.objects.filter(marks__lt=35)   
    #students=Student.objects.filter(name__startswith='A')   
    #students=Student.objects.all().order_by('marks')   
     #students=Student.objects.all().order_by('-marks')   
    my_dict={'students':students}
    return render(request,'testapp/index.html',students)  