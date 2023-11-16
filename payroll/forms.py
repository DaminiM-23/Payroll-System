from django import forms
from .models import Employee_details ,Salary
from django.contrib.auth.models import User

class Employee_details_Form(forms.ModelForm):         
    class Meta:
        model = Employee_details
        fields = '__all__'
        
class Salary_Form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'




