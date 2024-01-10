from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render , redirect, HttpResponseRedirect , get_object_or_404
from django.views.generic.edit import CreateView
from .models  import Employee_details ,Salary , staff_type , rule_man
from .forms import Employee_details_Form , Salary_Form , rule_man_Form , staff_type_Form
from django.contrib import messages
from django.core import validators

# Create your views here.
def base(request):
    return render(request,"base.html")

def e_n_drules(request): 
    return render(request,'e_n_drules.html')

def add_edit_subpay(request):
    return render(request,'add_edit_subpay.html')
   
def staff(request): 
    return render(request,'staff.html')
    
def supp_head(request): 
    return render(request,'supp_head.html')

def appoint(request): 
    return render(request,'appoint.html')

def transaction_mngt(request): 
    return render(request,'transaction_mngt.html')

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


def employee_registration_view(request):
    if request.method == 'POST':
        form = Employee_details_Form(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the model
            messages.success(request, 'Employee Registered successfully!')
            # return redirect('success.html')  # Redirect to a success page
            form = Employee_details_Form()
            return redirect('employee_registration') 
    else:
        form = Employee_details_Form()
    return render(request, 'employee_registration.html', {'form': form})

    
def staff_type_view(request):
    if request.method == 'POST':
        form = staff_type_Form(request.POST)
        if form.is_valid():
            st=form.cleaned_data['stafftype']
            reg=staff_type(stafftype=st)
            reg.save()   # Save the data to the model
            form = staff_type_Form()
            messages.success(request, 'Staff Type added successfully!')
            # return redirect('success.html')  # Redirect to a success page
            return redirect('staff_type') 
    else:
        form = staff_type_Form()
    staff_type_data = staff_type.objects.all()
    return render(request, 'staff_type.html', {'form': form,'staff_type_data':staff_type_data})


#for saving and retriveing data (rule management template)
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




    


class Salary_View(CreateView): 
   model=Salary
   form_class= Salary_Form
   #template_name='demo3.html'
   #fields='__all__'
   #success_url = '/demo4'

# def id_change(request):
#     id_no_obj, created=Employee_details.objects.get_or_create(pk=1, defaults={'id_no':0})
#     return render(request, 'employee_registration.html',{'id_no':id_no_obj.id_no})

# def update_id_no(request):
#     if request.method == 'POST' and request.is_ajax():
#         new_id = request.POST.get('id_no')
#         id_no_object = Employee_details.objects.get(pk=1)
#         id_no_object.last_id = new_id
#         id_no_object.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})



