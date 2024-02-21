from django.contrib import admin
from .models import *

class obj_Employee_details(admin.ModelAdmin):
    list_display=['id','employee_type','sequence_no','title','first_name','middle_name','last_name',
                  'date_of_birth','gender','aadhar_id','pan_no','email','mobile_no','address','date_of_joining', 'date_of_relieving','date_of_increment',
                  'date_of_retirement', 'from_appointment_date', 'to_appointment_date',
                  'designation_nature',  'department','designation' ,'appointment',
                  'staff_type','TA','HRA','handicap','quarter','senior_citizen',
                  'bank_acc_no','ifsc_code','bank','bank_branch',
                  'epf','gpf_no','dcps_no','rule','pay_level','cell_number',
                  'basic','pay_status','grade_pay']

admin.site.register(Employee_details,obj_Employee_details)
# admin.site.register(Employee_details)

class obj_satff_type(admin.ModelAdmin):
    list_display=['stafftype','retirement_age']

   
admin.site.register(staff_type,obj_satff_type)
admin.site.register(des_nature)
admin.site.register(appointment)
admin.site.register(department)
admin.site.register(designation)
admin.site.register(payhead_deduction)
admin.site.register(payhead_earning)
admin.site.register(deduction_rule)  
admin.site.register(earning_rule)
admin.site.register(bank)

class obj_PayLevelMaster(admin.ModelAdmin):
    list_display=['id','staff_type','pay_level','cell_1','cell_2','cell_3','cell_4','cell_5','cell_6','cell_7','cell_8','cell_9','cell_10','cell_11', 'cell_12', 'cell_13', 'cell_14', 'cell_15', 'cell_16', 'cell_17', 'cell_18', 'cell_19', 'cell_20', 'cell_21', 'cell_22', 'cell_23', 'cell_24', 'cell_25', 'cell_26', 'cell_27', 'cell_28', 'cell_29', 'cell_30', 'cell_31', 'cell_32', 'cell_33', 'cell_34', 'cell_35', 'cell_36', 'cell_37', 'cell_38', 'cell_39', 'cell_40']
    
admin.site.register(PayLevelMaster,obj_PayLevelMaster) 


class obj_rule_man(admin.ModelAdmin):
    list_display=['pay_rule','rule_name']
admin.site.register(rule_man,obj_rule_man)
