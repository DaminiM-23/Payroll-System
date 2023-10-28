from django.shortcuts import render , HttpResponse

# Create your views here.
def base(request): 
    return render(request,'base.html')

def login(request):
    return render(request, 'login.html')

# Added e and d rules views link
def e_n_drules(request):
    return render(request, 'e_n_drules.html')

# Added emp_reg rules
def empreg(request):
    return render(request, 'emp_reg.html')