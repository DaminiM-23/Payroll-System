from django.shortcuts import render , HttpResponse
from django.views.generic.edit import CreateView
from .models  import Employee_details

# Create your views here.
def base(request): 
    return render(request,'base.html')

def login(request): 
    return render(request,'login.html')

def e_n_drules(request): 
    return render(request,'e_n_drules.html')

class employee_registration_View(CreateView): 
   model=Employee_details
   template_name='employee_registration.html'
   fields=['title','first_name','middle_name','last_name']
    






