from django.urls import reverse
from django.shortcuts import render , HttpResponse
from django.views.generic.edit import CreateView
from .models  import Employee_details ,Salary
from .forms import Employee_details_Form , Salary_Form


# Create your views here.

def base(request):
    data={
        'title':'{% block title %}Base Template{% endblock %}',
        'Institute':'Veermata Jeejabai Technological Institute',
        'Address':'H R Mahajani Rd, Matunga, Mumbai, Maharashtra 400019'
        }
    return render(request,"base.html",data)

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
    data={
         'h5':'Supplementary Head Management',
         'formlabel':'Supplementary :'
         }
    return render(request,'supp_head.html',data)

def appoint(request): 
    data={
        'h5':'Add/Edit Appointment',
        'formlabel':'Appointment Type :'
    }
    return render(request,'appoint.html',data)

def transaction_mngt(request): 
    return render(request,'transaction_mngt.html')

def pay_level(request): 
    return render(request,'pay_level.html')

def department(request): 
    data={
        'h5':'Department Management',
        'formlabel1':'Sub Department:',
        'formlabel2':'Short Name:',
        'btn btn-primary':'Submit',
        'btn btn-warning':'Cancel',
        'btn btn-danger': 'Report'
        }
    return render(request,'department.html',data)

def account_head(request): 
    data={
        'h5':'Account Head Management',
        'formlabel1':'Account head:',
        'formlabel2':'Account No:'

    }
    return render(request,'account_head.html',data)

def quarter_type(request): 
    return render(request,'quarter_type.html')

def payment_head(request): 
    return render(request,'payment_head.html')


class employee_registration_View(CreateView): 
   
   model=Employee_details
   form_class= Employee_details_Form
   template_name='employee_registration.html'
   #fields='__all__'
   #success_url = '/demo2'

    
class Salary_View(CreateView): 
   model=Salary
   form_class= Salary_Form
   template_name='demo3.html'
   #fields='__all__'
   #success_url = '/demo4'





