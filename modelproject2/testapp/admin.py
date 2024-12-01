from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','e_name','e_sal','e_addr']
admin.site.register(Employee,EmployeeAdmin)

