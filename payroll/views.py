from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render , redirect, HttpResponse ,get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from .models  import *
from .forms import *
from django.contrib import messages
from django.core import validators 
from django.views.decorators.http import require_GET

def base(request):
    return render(request,"base.html")

def employee_registration_view(request):  
    pay_level_data = PayLevelMaster.objects.all()
    cell_numbers = range(1, 41) 
    rule_data = rule_man.objects.all()
    department_data = department.objects.all() 
    staff_type_data=staff_type.objects.all()
    designation_data=designation.objects.all()  
    des_nature_data=des_nature.objects.all()  
    appointment_data=appointment.objects.all() 
    bank_data=bank.objects.all() 
    last_id = Employee_details.objects.latest('id').id 
    latest_id = last_id + 1     
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
    return render(request, 'employee_registration.html',{'form': form,'latest_id': latest_id,'pay_level_data': pay_level_data,'cell_numbers': cell_numbers,'rule_data': rule_data,'staff_type_data':staff_type_data,'department_data': department_data,'designation_data': designation_data,'des_nature_data': des_nature_data,'appointment_data':appointment_data,'bank_data': bank_data})


def get_basic_value(request):
    pay_level = request.GET.get('pay_level')
    cell_number = request.GET.get('cell_number')

    try:
        pay_level_master = PayLevelMaster.objects.get(pay_level=pay_level)
        basic_value = getattr(pay_level_master, f'cell_{cell_number}')
        return JsonResponse({'basic_value': basic_value})
    except PayLevelMaster.DoesNotExist:
        return JsonResponse({'error': 'Pay level not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)







        

 
def staff_type_view(request):
    if request.method == 'POST':
        form = staff_type_Form(request.POST)
        if form.is_valid():
            st=form.cleaned_data['stafftype'] 
            ra=form.cleaned_data['retirement_age']
            reg=staff_type(stafftype=st,retirement_age=ra)
            reg.save()   
            form = staff_type_Form()
            messages.success(request, 'Staff Type added successfully!')
            return redirect('staff_type') 
    else:
        form = staff_type_Form()
    staff_type_data = staff_type.objects.all()
    return render(request, 'staff_type.html', {'form': form,'staff_type_data':staff_type_data})



def rule_man_view(request):
    if request.method == 'POST':
        fm = rule_man_Form(request.POST)
        if fm.is_valid():
            pr=fm.cleaned_data['pay_rule']
            rm=fm.cleaned_data['rule_name']
            reg=rule_man(pay_rule=pr, rule_name=rm)
            reg.save()  
            messages.success(request, 'Pay Rule added successfully!')
            return redirect('rule_man') 
            
    else:
        fm = rule_man_Form()
    rule_data = rule_man.objects.all()
    return render(request, 'rule_man.html', {'form': fm,'rule_data': rule_data})

def update_rule_view(request, pk):
    if request.method == 'POST':
        field = request.POST.get('field')
        value = request.POST.get('value')
        rule_instance = rule_man.objects.get(pk=pk)
        if field == 'pay_rule':
            rule_instance.pay_rule = value
        elif field == 'rule_name':
            rule_instance.rule_name = value
        rule_instance.save()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def pay_level_view(request):
    staff_type_data=staff_type.objects.all()
    pay_level_data = PayLevelMaster.objects.all()
    if request.method == 'POST':
        fm = PayLevelMaster_Form(request.POST)
        if fm.is_valid():
            s=fm.cleaned_data['staff_type']
            pl=fm.cleaned_data['pay_level']  
            reg=PayLevelMaster(staff_type=s, pay_level=pl)
            reg.save() 
            return redirect('pay_level')  
            
    else:
        fm = PayLevelMaster_Form()
    return render(request, 'pay_level.html', {'form': fm,'pay_level_data': pay_level_data,'staff_type_data':staff_type_data})


class DisplayCellValuesView(View):    
    def post(self, request, *args, **kwargs):
        form = DisplayCellValuesForm(request.POST)
        if form.is_valid():
            pay_level_id = form.cleaned_data['pay_level_id']
            pay_level_instance = get_object_or_404(PayLevelMaster, id=pay_level_id)
            cell_values = [pay_level_instance.cell_1, pay_level_instance.cell_2, pay_level_instance.cell_3, pay_level_instance.cell_4, pay_level_instance.cell_5, pay_level_instance.cell_6, pay_level_instance.cell_7, pay_level_instance.cell_8, pay_level_instance.cell_9, pay_level_instance.cell_10, pay_level_instance.cell_11,pay_level_instance.cell_12,pay_level_instance.cell_13,pay_level_instance.cell_14,pay_level_instance.cell_15,pay_level_instance.cell_16,pay_level_instance.cell_17,pay_level_instance.cell_18,pay_level_instance.cell_19,pay_level_instance.cell_20,pay_level_instance.cell_21,pay_level_instance.cell_22,pay_level_instance.cell_23,pay_level_instance.cell_24,pay_level_instance.cell_25,pay_level_instance.cell_26,pay_level_instance.cell_27,pay_level_instance.cell_28,pay_level_instance.cell_29,pay_level_instance.cell_30,pay_level_instance.cell_31,pay_level_instance.cell_32,pay_level_instance.cell_33,pay_level_instance.cell_34,pay_level_instance.cell_35,pay_level_instance.cell_36,pay_level_instance.cell_37,pay_level_instance.cell_38,pay_level_instance.cell_39,pay_level_instance.cell_40]
            enumerated_cell_values = enumerate(cell_values)
            return render(request, 'basic_amount.html', {'pay_level_data': PayLevelMaster.objects.all(), 'cell_values':  enumerated_cell_values})







def department_view(request):
        if request.method == 'POST':
            fm = department_Form(request.POST)
            if fm.is_valid():
                dn=fm.cleaned_data['dep_name']
                reg=department(dep_name=dn)
                reg.save()  # Save the data to the model
                return redirect('department')  # Redirect to a success page
                
        else:
            fm = department_Form()
        department_data= department.objects.all()
        return render(request, 'department.html', {'form': fm,'department_data': department_data})

def designation_view(request):
        if request.method == 'POST':
            fm = designation_Form(request.POST)
            if fm.is_valid():
                des=fm.cleaned_data['designation']
                reg=designation(designation=des)
                reg.save()
                fm = designation_Form()  # Save the data to the model
                return redirect('designation')  # Redirect to a success page
                
        else:
            fm = designation_Form()
        designation_data= designation.objects.all()
        return render(request, 'designation.html', {'form': fm,'designation_data': designation_data})

def des_nature_view(request):
        if request.method == 'POST':
            fm = des_nature_Form(request.POST)
            if fm.is_valid():
                desn=fm.cleaned_data['des_nature']
                reg=des_nature(des_nature=desn)
                reg.save()
                fm = des_nature_Form()  # Save the data to the model
                return redirect('des_nature')  # Redirect to a success page
                
        else:
            fm = des_nature_Form()
        des_nature_data= des_nature.objects.all()
        return render(request, 'des_nature.html', {'form': fm,'des_nature_data': des_nature_data}) 

def appointment_view(request):
        if request.method == 'POST':
            fm = appointment_Form(request.POST)
            if fm.is_valid():
                ap=fm.cleaned_data['appointment']
                reg=appointment(appointment=ap)
                reg.save()
                form = appointment_Form()  # Save the data to the model
                return redirect('appointment')  # Redirect to a success page
               
        else:
            fm = appointment_Form()
        appointment_data= appointment.objects.all()
        return render(request, 'appointment.html', {'form': fm,'appointment_data': appointment_data})

def bank_view(request):
        if request.method == 'POST':
            fm = bank_Form(request.POST)
            if fm.is_valid():
                des=fm.cleaned_data['bank']
                reg=bank(bank=des)
                reg.save()
                fm = bank_Form()  # Save the data to the model
                return redirect('bank')  # Redirect to a success page
               
        else:
            fm = bank_Form()
        bank_data= bank.objects.all()
        return render(request, 'bank.html', {'form': fm,'bank_data': bank_data})

def earning_rule_view(request): 
    rule_data = rule_man.objects.all()
    payhead_e= payhead_earning.objects.all()
    if request.method == 'POST':
        fm = earning_rule_Form(request.POST)           
        if fm.is_valid():  
            r=fm.cleaned_data['rule']
            c=fm.cleaned_data['cal']
            p=fm.cleaned_data['per']
            hd=fm.cleaned_data['head_earning']
            ed=fm.cleaned_data['eff_date']
            reg=earning_rule(rule=r,cal=c,per=p,head_earning=hd,eff_date=ed)
            reg.save()  # Save the data to the model  
            messages.success(request, 'successfull!')                 
            return redirect('earning_rule')                         
    else:
        fm = earning_rule_Form()    
    earning_rule_data= earning_rule.objects.all()    
    return render(request, 'earning_rule.html',{'form': fm,'rule_data': rule_data,'payhead_e':payhead_e,'earning_rule_data':earning_rule_data})

def deduction_rule_view(request): 
    rule_data = rule_man.objects.all()
    payhead_d= payhead_deduction.objects.all()
    if request.method == 'POST':
        fm = deduction_rule_Form(request.POST)           
        if fm.is_valid():  
            r=fm.cleaned_data['rule']
            c=fm.cleaned_data['cal']
            p=fm.cleaned_data['per']
            hd=fm.cleaned_data['head_deduction']
            ed=fm.cleaned_data['eff_date']
            reg=deduction_rule(rule=r,cal=c,per=p,head_deduction=hd,eff_date=ed)
            reg.save()  # Save the data to the model  
            messages.success(request, 'successfull!')                 
            return redirect('deduction_rule')                         
    else:
        fm = deduction_rule_Form()    
    deduction_rule_data= deduction_rule.objects.all()    
    return render(request, 'deduction_rule.html',{'form': fm,'rule_data': rule_data,'payhead_d':payhead_d,'deduction_rule_data':deduction_rule_data})

    
def payhead_earning_view(request):
        if request.method == 'POST':     
            fm = payhead_earning_Form(request.POST)
            if fm.is_valid(): 
                ph=fm.cleaned_data['pay_head']
                fn=fm.cleaned_data['f_name']
                reg=payhead_earning(pay_head=ph,f_name=fn)
                reg.save()
                fm = payhead_earning_Form()  
                return redirect('payhead_earning')  
        else:
            fm = payhead_earning_Form()
        payhead_e= payhead_earning.objects.all()
        return render(request, 'payhead_earning.html', {'form': fm,'payhead_e': payhead_e})

def payhead_deduction_view(request):
        if request.method == 'POST':     
            fm = payhead_deduction_Form(request.POST)
            if fm.is_valid(): 
                ph=fm.cleaned_data['pay_head']
                fn=fm.cleaned_data['f_name']
                reg=payhead_deduction(pay_head=ph,f_name=fn)
                reg.save()
                fm = payhead_deduction_Form()  
                return redirect('payhead_deduction')  
        else:
            fm = payhead_deduction_Form()
        payhead_d= payhead_deduction.objects.all()
        return render(request, 'payhead_deduction.html', {'form': fm,'payhead_d': payhead_d})

def payment_head_view(request):  
    if request.method == 'POST':
            fm = payment_head_Form(request.POST)
            if fm.is_valid(): 
                # pc=fm.cleaned_data['Paycode']
                h=fm.cleaned_data['head']
                t=fm.cleaned_data['type']
                c=fm.cleaned_data['cal']
                reg=payment_head(head=h,type=t,cal=c)
                reg.save()
                fm = payment_head_Form()  
                return redirect('payment_head')  
    else:
            fm = payment_head_Form()   
    pay_head_data=payhead_earning.objects.all()    
    payment_head_data=payment_head.objects.all()
    return render(request,'payment_head.html',{'form': fm,'pay_head_data':pay_head_data,'payment_head_data':payment_head_data})


 

