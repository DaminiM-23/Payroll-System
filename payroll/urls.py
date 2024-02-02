from django.contrib import admin 
from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import *
from payroll import views

  
urlpatterns = [ 
    path('base', views.base,name='base'),    
    path('', views.employee_registration_view ,name='employee_registration'),
    path('rule_man',views.rule_man_view,name='rule_man'),
    path('update_rule/<int:pk>/',views.update_rule_view,name='update_rule'),
    path('bank',views.bank_view ,name='bank'),
    path('staff_type',views.staff_type_view ,name='staff_type'),
    path('payhead_earning',views.payhead_earning_view ,name='payhead_earning'),    
    path('payhead_deduction',views.payhead_deduction_view ,name='payhead_deduction'),
    path('deduction_rule', views.deduction_rule_view ,name='deduction_rule'),
    path('earning_rule', views.earning_rule_view ,name='earning_rule'),
    path('appointment',views.appointment_view ,name='appointment'),
    path('pay_level',views.pay_level_view ,name='pay_level'),
    path('display_cell_values/', DisplayCellValuesView.as_view(), name='display_cell_values'), 
    
    path('department',views.department_view ,name='department'),
    path('designation',views.designation_view ,name='designation'),
    path('des_nature',views.des_nature_view ,name='des_nature'),
    path('des_nature',views.des_nature_view ,name='des_nature'),
    path('payment_head',views.payment_head_view ,name='payment_head'),  
    
] 
 