
from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
<<<<<<< HEAD
from .views import employee_registration_View
=======
from .views import employee_registration_View ,Salary_View
>>>>>>> fee6b166fa1d56c22e6964ead6a390b5cacc3cb7
from payroll import views

  
urlpatterns = [ 
    path('', views.login, name='login'),
    path('base', views.base,name='base'),
    path('e_n_drules', views.e_n_drules ,name='e_n_drules'),
    path('employee_registration', employee_registration_View.as_view() ,name='employee_registration'),
<<<<<<< HEAD
    path('payment_head',views.payment_head,name='payment_head' ),
=======
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
>>>>>>> fee6b166fa1d56c22e6964ead6a390b5cacc3cb7
] 
