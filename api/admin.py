from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class companyadmin(admin.ModelAdmin):
    list_display=('name','locations','type')


class employeesadmin(admin.ModelAdmin):
    list_display=('name','email','company')    

admin.site.register(Company,companyadmin)
admin.site.register(Employee,employeesadmin)