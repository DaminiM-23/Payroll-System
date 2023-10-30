from django.contrib import admin
from .models import (Employee_details,User_login,Salary)

class obj_Employee_details(admin.ModelAdmin):
    list_display=['title','first_name','middle_name','last_name','father_name',
                  'date_of_birth','gender','jntu_no','acite_id','employee_no',
                  'aadhar_or_unique_id','email','cell_no','Bloodgroup','date_of_joining', 'date_of_relieving','date_of_increment',
                  'pay_revised_date', 'date_of_retirement', 'from_appointment_date', 'to_appointment_date',
                  'designation_nature',  'department','designation' ,'appointment','department','designation','appointment',
                  'staff_type','bank_name','vocational','bank_branch','user_type','appoint_in',
                  'TA','handicap','quarter','senior_citizen','quarter_rent','quarter_type','bank_acc_no',
                  'ifsc_code','epf','ppf_no','pf_no','pan_no','rule','scale','pay_level','cell_number',
                  'basic','pay_status','grade_pay','remark']




class obj_salary(admin.ModelAdmin):
    list_display=['Salary']



admin.site.register(User_login)
admin.site.register(Employee_details,obj_Employee_details)
admin.site.register(Salary,obj_salary)


