from django.contrib import admin
from .models import (Employee_details,Salary,staff_type,rule_man )

class obj_Employee_details(admin.ModelAdmin):
    list_display=['id_no','employee_type','sequence_no','title','first_name','middle_name','last_name',
                  'date_of_birth','gender','aadhar_id','pan_no','email','mobile_no','address','date_of_joining', 'date_of_relieving','date_of_increment',
                  'date_of_retirement', 'from_appointment_date', 'to_appointment_date',
                  'designation_nature',  'department','designation' ,'appointment',
                  'staff_type','TA','HRA','handicap','quarter','senior_citizen','quarter_type',
                  'bank_acc_no','ifsc_code','bank_name','bank_branch',
                  'epf','gpf_no','dcps_no','rule','pay_level','cell_number',
                  'basic','pay_status','grade_pay']




class obj_salary(admin.ModelAdmin):
    list_display=['Salary']

admin.site.register(Employee_details,obj_Employee_details)
admin.site.register(Salary,obj_salary)

admin.site.register(staff_type)

class obj_rule_man(admin.ModelAdmin):
    list_display=['pay_rule','rule_name']
admin.site.register(rule_man,obj_rule_man)
