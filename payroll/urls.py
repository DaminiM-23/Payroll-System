
from django.contrib import admin 
from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import *
from payroll import views

  
urlpatterns = [ 
    # path('demoform', views.demoform_view,name='demoform'),
    path('base', views.base,name='base'),
    path('e_n_drules', views.e_n_drules ,name='e_n_drules'),
    path('', views.employee_registration_view ,name='employee_registration'),
    path('add_edit_subpay',views.add_edit_subpay ,name='add_edit_subpay'),
    path('rule_man',views.rule_man_view,name='rule_man'),
    path('update_rule/<int:pk>/',views.update_rule_view,name='update_rule'),
    path('staff',views.staff ,name='staff'),
    # path('success',views.success ,name='success'),
    path('staff_type',views.staff_type_view ,name='staff_type'),
    path('supp_head',views.supp_head ,name='supp_head'),
    path('appointment',views.appointment_view ,name='appointment'),
    path('transaction_mngt',views.transaction_mngt ,name='transaction_mngt'),
    path('pay_level',views.pay_level_view ,name='pay_level'),
    path('pay_level',views.basic_amount_view ,name='basic_amount'),
    path('pay_scale',views.pay_scale_view ,name='pay_scale'),
    path('department',views.department_view ,name='department'),
    path('designation',views.designation_view ,name='designation'),
     path('des_nature',views.des_nature_view ,name='des_nature'),
    path('des_nature',views.des_nature_view ,name='des_nature'),
    path('account_head',views.account_head ,name='account_head'),
    path('quarter_type',views.quarter_type ,name='quarter_type'),
    path('payment_head',views.payment_head ,name='payment_head'),
    # path('id_change',views.id_change, name='id_change'),
    # path('update_id_no',views.update_id_no, name='update_id_no'),
    #path('demo3', Salary_View.as_view() ,name='Salary_View'),
] 
