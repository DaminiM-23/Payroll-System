
from django.contrib import admin 
from django.urls import path 
  
# importing views from views..py 
from payroll import views

  
urlpatterns = [ 
    path('', views.login ,name='login'),
    path('base', views.base, name="base"),
    path('endrules', views.e_n_drules, name="endrules"),
    path('empreg', views.empreg, name='employee registration'),
] 