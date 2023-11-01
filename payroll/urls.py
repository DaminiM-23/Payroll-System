
from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from .views import employee_registration_View ,Salary_View
from payroll import views

  
urlpatterns = [ 
    path('', views.login, name='login'),
    path('base', views.base,name='base'),
    path('e_n_drules', views.e_n_drules ,name='e_n_drules'),
    path('demo', employee_registration_View.as_view() ,name='employee_registration'),
    #path('demo3', Salary_View.as_view() ,name='Salary_View'),
] 
