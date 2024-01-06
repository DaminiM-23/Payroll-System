from django import forms
from .models import Employee_details ,Salary 
from django.contrib.auth.models import User
       


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
             'first_name':forms.TextInput(attrs={'class': 'form-control'}),
             'gender':forms.Select(attrs={'class': 'form-control'}),
             'sequence_no':forms.TextInput(attrs={'class': 'form-control'}),
             'aadhar_id':forms.TextInput(attrs={'class': 'form-control'}),
             'pan_no':forms.TextInput(attrs={'class': 'form-control'}),
             'email':forms.TextInput(attrs={'class': 'form-control'}),
             'mobile_no':forms.TextInput(attrs={'class': 'form-control'}),
             'address':forms.TextInput(attrs={'class': 'form-control'}),
             'designation_nature' :forms.Select(attrs={'class': 'form-control'}),
             'department':forms.Select(attrs={'class': 'form-control'}),
             'designation':forms.Select(attrs={'class': 'form-control'}),
             'appointment':forms.Select(attrs={'class': 'form-control'}),
             'staff_type':forms.Select(attrs={'class': 'form-control'}),
             'quarter_type':forms.Select(attrs={'class': 'form-control'}),
             'bank_acc_no':forms.TextInput(attrs={'class': 'form-control',}),
             'ifsc_code':forms.TextInput(attrs={'class': 'form-control',}),
             'bank_name':forms.Select(attrs={'class': 'form-control',}),
             'bank_branch':forms.TextInput(attrs={'class': 'form-control',}),
             'epf':forms.TextInput(attrs={'class': 'form-control',}),
             'gpf_no':forms.TextInput(attrs={'class': 'form-control',}),
             'dcps_no':forms.TextInput(attrs={'class': 'form-control',}),
             'rule':forms.Select(attrs={'class': 'form-control',}),
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
        

class Staff_Mngt_Form(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['staff_type']

# class demoform_Form(forms.ModelForm):         
#     class Meta:
#         model = demo
#         fields = '__all__'

       

