from django.urls import reverse_lazy
from django.shortcuts import render , redirect, HttpResponseRedirect , get_object_or_404
from django.views.generic.edit import CreateView
from .models  import Employee_details ,Salary , staff_type , rule_man
from .forms import Employee_details_Form , Salary_Form , rule_man_Form , staff_type_Form
from django.contrib import messages
from django.core import validators


# Create your views here.
def base(request):
    data={
        'title':'Base Template',
        'Institute':'Veermata Jeejabai Technological Institute',
        'Address':'H R Mahajani Rd, Matunga, Mumbai, Maharashtra 400019'
        }
    return render(request,"base.html",data)



def e_n_drules(request): 
    return render(request,'e_n_drules.html')


def add_edit_subpay(request):
    return render(request,'add_edit_subpay.html')
   
def rule_man_view(request):
    if request.method == 'POST':
        fm = rule_man_Form(request.POST)
        if fm.is_valid():
            pr=fm.cleaned_data['pay_rule']
            rm=fm.cleaned_data['rule_name']
            reg=rule_man(pay_rule=pr, rule_name=rm)
            reg.save()  # Save the data to the model
            messages.success(request, 'Pay Rule added successfully!')
            return redirect('rule_man')  # Redirect to a success page
            fm = rule_man_Form()
    else:
        fm = rule_man_Form()
    rule_data = rule_man.objects.all()
    return render(request, 'rule_man.html', {'form': fm,'rule_data': rule_data})

def staff(request): 
    return render(request,'staff.html')
    

# def staff_man(request): 
#     return render(request,'staff_man.html')

# def staff_man(request):
#     if request.method == 'POST':
#         form = Staff_Mngt_Form(request.POST)
#         if form.is_valid():
#             form.save()  # Save the data to the model
#             # messages.success(request, 'Employee Registered successfully!')
#             # return redirect('success.html')  # Redirect to a success page
#             form = Staff_Mngt_Form()
#     else:
#         form = Staff_Mngt_Form()
#     return render(request, 'employee_registration.html', {'form': form})



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


def employee_registration_view(request):
    if request.method == 'POST':
        form = Employee_details_Form(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the model
            messages.success(request, 'Employee Registered successfully!')
          
            form = Employee_details_Form()
    else:
        form = Employee_details_Form()
    return render(request, 'employee_registration.html', {'form': form})

    
class Salary_View(CreateView): 
   model=Salary
   form_class= Salary_Form
   #template_name='demo3.html'
   #fields='__all__'
   #success_url = '/demo4'





