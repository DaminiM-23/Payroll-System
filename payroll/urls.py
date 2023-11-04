
from django.contrib import admin 
from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import employee_registration_View ,Salary_View
from payroll import views

  
urlpatterns = [ 
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('base', views.base,name='base'),
    path('e_n_drules', views.e_n_drules ,name='e_n_drules'),
    path('employee_registration', employee_registration_View.as_view() ,name='employee_registration'),
    path('add_edit_subpay',views.add_edit_subpay ,name='add_edit_subpay'),
    path('rule_man',views.rule_man ,name='rule_man'),
    path('staff',views.staff ,name='staff'),
    path('staff_man',views.staff_man ,name='staff_man'),
    path('supp_head',views.supp_head ,name='supp_head'),
    path('appoint',views.appoint ,name='appoint'),
    path('transaction',views.transaction ,name='transaction'),
    path('pay_level',views.pay_level ,name='pay_level'),
    path('department',views.department ,name='department'),
    path('account_head',views.account_head ,name='account_head'),
    path('quarter_type',views.quarter_type ,name='quarter_type'),
    path('payment_head',views.payment_head ,name='payment_head'),
    #path('demo3', Salary_View.as_view() ,name='Salary_View'),
] 
