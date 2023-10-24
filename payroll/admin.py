from django.contrib import admin
from .models import (Employee_details,User_login,Salary)


admin.site.register(User_login)
admin.site.register(Employee_details)
admin.site.register(Salary)


