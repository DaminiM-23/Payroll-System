from typing import Self
from django import forms
from .models import *
# from django.contrib.auth.models import User
# from django.core import validators      


class Employee_details_Form(forms.ModelForm):         
    class Meta:
        model = Employee_details
        fields = '__all__'
        widgets={

             'date_of_birth':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'date_of_joining':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'date_of_relieving':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'date_of_increment':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'date_of_retirement':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'from_appointment_date':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'to_appointment_date':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
             'TA': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')],),
             'handicap': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'quarter': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'senior_citizen': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'pay_status': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'employee_type':forms.Select(attrs={'class': 'form-control',}),
             'id_no':forms.TextInput(attrs={'class': 'form-control'}),
             #For the image upload
             'photo':forms.FileInput(attrs={'class': 'form-control-file',}),
             #Sign ka new variable
             'sign':forms.FileInput(attrs={'class': 'form-control-file',}),
             'title':forms.Select(attrs={'class': 'form-control'}),
             'middle_name':forms.TextInput(attrs={'class': 'form-control'}),
             'last_name':forms.TextInput(attrs={'class': 'form-control'}),
             'first_name':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name','autocomplete': 'name'}),
             'gender':forms.Select(attrs={'class': 'form-control'}),
             'sequence_no':forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
             'aadhar_id':forms.TextInput(attrs={'class': 'form-control'}),
             'pan_no':forms.TextInput(attrs={'class': 'form-control'}),
             'email':forms.TextInput(attrs={'class': 'form-control'}),
             'mobile_no':forms.TextInput(attrs={'class': 'form-control'}),
             'address':forms.Textarea(attrs={'class':  'form-control form-horizontal','rows': 1}),
             'designation_nature' :forms.TextInput(attrs={'class': 'form-control'}),
             'department':forms.TextInput(attrs={'class': 'form-control',}),
             'designation':forms.TextInput(attrs={'class': 'form-control'}),
             'appointment':forms.TextInput(attrs={'class': 'form-control'}),
             'staff_type':forms.TextInput(attrs={'class': 'form-control'}),
             'quarter_type':forms.Select(attrs={'class': 'form-control'}),
             'bank_acc_no':forms.TextInput(attrs={'class': 'form-control',}),
             'ifsc_code':forms.TextInput(attrs={'class': 'form-control',}),
             'bank_name':forms.Select(attrs={'class': 'form-control',}),
             'bank_branch':forms.TextInput(attrs={'class': 'form-control',}),
             'epf':forms.TextInput(attrs={'class': 'form-control',}),
             'gpf_no':forms.TextInput(attrs={'class': 'form-control',}),
             'dcps_no':forms.TextInput(attrs={'class': 'form-control',}),
             'rule':forms.TextInput(attrs={'class': 'form-control',}),
             'pay_level':forms.Select(attrs={'class': 'form-control',}),
             'cell_number':forms.Select(attrs={'class': 'form-control',}),
             'basic':forms.TextInput(attrs={'class': 'form-control',}),
             'pay_status':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')],),
             'grade_pay':forms.TextInput(attrs={'class': 'form-control',}),
             'HRA':forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')],)
              }
         
        



class Salary_Form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
        

class staff_type_Form(forms.ModelForm):
    class Meta:
        model = staff_type
        fields = ['stafftype']
        widgets={
            'stafftype':forms.TextInput(attrs={'class': 'form-control'})
            }

class rule_man_Form(forms.ModelForm):
    class Meta:
        model = rule_man
        fields = [ 'pay_rule','rule_name']
        widgets={
            'pay_rule':forms.TextInput(attrs={'class': 'form-control'}),
            'rule_name':forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class PayLevelMaster_Form(forms.ModelForm):
    class Meta:
        model = PayLevelMaster
        fields = [ 'staff_type','pay_level']
        widgets={
            'staff_type':forms.TextInput(attrs={'class': 'form-control'}),
            'pay_level':forms.TextInput(attrs={'class': 'form-control'}),
        }


class department_Form(forms.ModelForm):
    class Meta:
        model = department
        fields = [ 'dep_name']
        widgets={
            'dep_name':forms.TextInput(attrs={'class': 'form-control'}),
           
            # 'des_nature':forms.TextInput(attrs={'class': 'form-control'}),       
        }
class designation_Form(forms.ModelForm):
    class Meta:
        model = designation
        fields = ['designation']
        widgets={   
            'designation':forms.TextInput(attrs={'class': 'form-control'}),
        }

class des_nature_Form(forms.ModelForm):
    class Meta:
        model = des_nature
        fields = ['des_nature']
        widgets={   
            'des_nature':forms.TextInput(attrs={'class': 'form-control'}),
        }

class basic_amount_Form(forms.ModelForm):         
    class Meta:
        model = basic_amount
        fields = '__all__'
        widgets={
            'basic_amount':forms.TextInput(attrs={'class': 'form-control'})}

class appointment_Form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['appointment']
        widgets={   
            'appointment':forms.TextInput(attrs={'class': 'form-control'}),
        }


       

# class EmployeeForm(forms.Form):
#     EMPLOYEE_TYPE_CHOICES = [
#         ('1', 'Permanent'),
#         ('2', 'Contractual Non-Teaching'),
#         ('3', 'Contractual Teaching'),
#         ('4', 'Security'),
#     ]
    
#     employee_type = forms.ChoiceField(choices=EMPLOYEE_TYPE_CHOICES)
#     sequence_no = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))