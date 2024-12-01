from django.shortcuts import render
from testapp.models import Employee

# Function-based view for displaying employees
def emp_view(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list': emp_list}
    return render(request, 'testapp/emp.html', context=my_dict)


