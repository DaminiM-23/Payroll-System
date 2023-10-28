
from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from payroll import views

  
urlpatterns = [ 
    path('', views.login, name='login'),
    path('base', views.base,name='base'),
    path('e_n_drules', views.e_n_drules ,name='e_n_drules'),
    path('employee_registration', views.employee_registration ,name='employee_registration'),
] 