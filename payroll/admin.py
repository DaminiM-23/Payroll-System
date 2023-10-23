from django.contrib import admin
from .models import (User_login,Employee_details,Salary)


# Register your models here.
admin.site.register(User_login)
admin.site.register(Employee_details)
admin.site.register(Salary)
#admin.site.register(Payslip)
