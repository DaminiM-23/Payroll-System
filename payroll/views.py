from django.urls import reverse
from django.shortcuts import render , HttpResponse
from django.views.generic.edit import CreateView
from .models  import Employee_details ,Salary
from .forms import Employee_details_Form , Salary_Form

# Create your views here.
def base(request): 
    return render(request,'base.html')


def login(request): 
    return render(request,'login.html')

def e_n_drules(request): 
    return render(request,'e_n_drules.html')

class employee_registration_View(CreateView): 
   model=Employee_details
   form_class= Employee_details_Form
   template_name='employee_registration.html'





#class Salary_View(CreateView): 
 #  model=Salary
  # form_class= Salary_Form
   






