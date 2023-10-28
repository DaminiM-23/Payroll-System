from django.db import models


class User_login(models.Model):
    user_name=models.CharField(max_length=30)



class Employee_details(models.Model):
    #PERSONAL_DETAILS
    title=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    