from django.shortcuts import render , HttpResponse

# Create your views here.
def base(request): 
    return render(request,'base.html')

def login(request): 
    return render(request,'login.html')

def e_n_drules(request): 
    return render(request,'e_n_drules.html')

def employee_registration(request): 
    return render(request,'employee_registration.html')

