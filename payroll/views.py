from django.shortcuts import render , HttpResponse

# Create your views here.
def base(request): 
    return render(request,'base.html')

def login(request):
    return render(request, 'login.html')