from django import forms
from .models import Employee_details ,Salary 
from django.contrib.auth.models import User
       


class Employee_details_Form(forms.ModelForm):         
    class Meta:
        model = Employee_details
        fields = '__all__'
        widgets={
             'date_of_birth':forms.DateInput(attrs={'type': 'date'}),
             'date_of_joining':forms.DateInput(attrs={'type': 'date'}),
             'date_of_relieving':forms.DateInput(attrs={'type': 'date'}),
             'date_of_increment':forms.DateInput(attrs={'type': 'date'}),
             'pay_revised_date':forms.DateInput(attrs={'type': 'date'}),
             'date_of_retirement':forms.DateInput(attrs={'type': 'date'}),
             'from_appointment_date':forms.DateInput(attrs={'type': 'date'}),
             'to_appointment_date':forms.DateInput(attrs={'type': 'date'}),
             'TA': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'handicap': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'quarter': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'senior_citizen': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'quarter_rent': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
             'pay_status': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),   
         

        }
        shift_joining = forms.ChoiceField( choices=Employee_details.SHIFT_CHOICES,widget=forms.RadioSelect,required=True)
        shift_relieving = forms.ChoiceField( choices=Employee_details.SHIFT_CHOICES,widget=forms.RadioSelect,required=True)


class Salary_Form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'



# class demoform_Form(forms.ModelForm):         
#     class Meta:
#         model = demo
#         fields = '__all__'
       

