
from typing import Self
from django import forms
from .models import *
  
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
             #Changed the input to allow preview image to connect to the uploaded image
             'photo': forms.FileInput(attrs={'class': 'form-control-file', 'onchange': 'previewImage(this)'}),
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
             'bank':forms.TextInput(attrs={'class': 'form-control',}),
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
        





        
class staff_type_Form(forms.ModelForm):
    class Meta:
        model = staff_type
        fields = ['stafftype','retirement_age']
        widgets={
            'stafftype':forms.TextInput(attrs={'class': 'form-control'}),
            'retirement_age':forms.TextInput(attrs={'class': 'form-control'})
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
            'dep_name':forms.TextInput(attrs={'class': 'form-control'}),
           
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

class DisplayCellValuesForm(forms.Form):
    pay_level_id = forms.IntegerField(widget=forms.HiddenInput())
 



class appointment_Form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['appointment']
        widgets={   
            'appointment':forms.TextInput(attrs={'class': 'form-control'}),
        }

class bank_Form(forms.ModelForm):
    class Meta:
        model = bank
        fields = ['bank']
        widgets={   
            'bank':forms.TextInput(attrs={'class': 'form-control'}),
        }



class payhead_earning_Form(forms.ModelForm):
    class Meta:
        model = payhead_earning
        fields = ['pay_head','f_name']
        widgets={   
            'pay_head':forms.TextInput(attrs={'class': 'form-control'}),
            'f_name':forms.TextInput(attrs={'class': 'form-control'})
        }

    
class payhead_deduction_Form(forms.ModelForm):
    class Meta:
        model = payhead_deduction
        fields = ['pay_head','f_name']
        widgets={   
            'pay_head':forms.TextInput(attrs={'class': 'form-control'}),
            'f_name':forms.TextInput(attrs={'class': 'form-control'})
        }    
   
class payment_head_Form(forms.ModelForm):
    class Meta:
        model = payment_head
        fields = ['head','type','cal']
        widgets={   
            # 'Paycode':forms.TextInput(attrs={'class': 'form-control'}),
            'head':forms.TextInput(attrs={'class': 'form-control'}),
            'type':forms.Select(attrs={'class': 'form-control'}),
            'cal':forms.TextInput(attrs={'class': 'form-control'})
        }

class deduction_rule_Form(forms.ModelForm):
    class Meta: 
        model = deduction_rule
        fields =['rule','cal','per','head_deduction','eff_date']
        widgets={   
            'rule':forms.TextInput(attrs={'class': 'form-control'}),
            'cal':forms.TextInput(attrs={'class': 'form-control'}),
            'per':forms.TextInput(attrs={'class': 'form-control'}),
            'head_deduction':forms.Select(attrs={'class': 'form-control'}),
            'eff_date':forms.DateInput(attrs={'type': 'date','class': 'form-control'})
        }

class earning_rule_Form(forms.ModelForm):
    class Meta:
        model = earning_rule
        fields =['rule','cal','per','head_earning','eff_date']
        widgets={   
            'rule':forms.TextInput(attrs={'class': 'form-control'}),
            'cal':forms.TextInput(attrs={'class': 'form-control'}),
            'per':forms.TextInput(attrs={'class': 'form-control'}),
            'head_earning':forms.Select(attrs={'class': 'form-control'}),
            'eff_date':forms.DateInput(attrs={'type': 'date','class': 'form-control'})
        } 