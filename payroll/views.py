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

def add_edit_subpay(request): 
    return render(request,'add_edit_subpay.html')

def rule_man(request): 
    return render(request,'rule_man.html')

def staff(request): 
    return render(request,'staff.html')

def staff_man(request): 
    return render(request,'staff_man.html')

def supp_head(request): 
    return render(request,'supp_head.html')

def appoint(request): 
    return render(request,'appoint.html')

def transaction(request): 
    return render(request,'transaction.html')

def pay_level(request): 
    return render(request,'pay_level.html')

def department(request): 
    return render(request,'department.html')

def account_head(request): 
    return render(request,'account_head.html')

def quarter_type(request): 
    return render(request,'quarter_type.html')

def payment_head(request): 
    return render(request,'payment_head.html')




class employee_registration_View(CreateView): 
   model=Employee_details
   form_class= Employee_details_Form
   template_name='employee_registration.html'







