from django.db import models


class Employee_details(models.Model):
    #PERSONAL_DETAILSS
    id_no=models.PositiveIntegerField(default=1000)
    title=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender=models.CharField(max_length=30)
    jntu_no=models.CharField(max_length=30 ,unique=True)
    acite_id=models.CharField(max_length=30 ,unique=True)
    employee_no=models.CharField(max_length=30)
    sequence_no=models.PositiveIntegerField(default=0)
    aadhar_or_unique_id=models.CharField(max_length=20 , unique=True)
    email = models.EmailField(max_length=30,unique=True)
    cell_no = models.CharField(max_length=20)
    Bloodgroup=models.CharField(max_length=10)
    #photo=models.ImageField()
    #sign=models.ImageField()

    #SERVICE_DATE_DETAILS
    date_of_joining = models.DateField()
    shift_joining=models.BooleanField(default=False)
    date_of_relieving = models.DateField()
    shift_relieving=models.BooleanField(default=False)
    date_of_increment = models.DateField(null=True)
    pay_revised_date  = models.DateField()
    date_of_retirement  = models.DateField()
    from_appointment_date = models.DateField()
    to_appointment_date = models.DateField()

    #SERVICE_TYEP_DETAILS
    designation_nature=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    appointment=models.CharField(max_length=30)
    staff_type=models.CharField(max_length=30)
    bank_name=models.CharField(max_length=30)
    vocational=models.CharField(max_length=30)
    bank_branch=models.CharField(max_length=30)
    user_type=models.CharField(max_length=30)
    appointed_in=models.CharField(max_length=30)

    #BASIC_DETAILS
    TA=models.BooleanField(default=True)
    handicap=models.BooleanField(default=False)
    quarter=models.BooleanField(default=False)
    senior_citizen=models.BooleanField(default=False)
    quarter_rent=models.BooleanField(default=True)
    quarter_type=models.CharField(max_length=30)

    #BANK_DETAILS
    bank_acc_no= models.CharField(max_length=20)
    ifsc_code =models.CharField(max_length=20)
    epf = models.CharField(max_length=20)
    ppf_no = models.CharField(max_length=20)
    pf_no = models.CharField(max_length=20)
    pan_no= models.CharField(max_length=20 , unique =True )

    #PAY_SCALE_DETAILS
    rule=models.CharField(max_length=30)
    scale=models.CharField(max_length=30)
    pay_level=models.CharField(max_length=30)
    cell_number=models.CharField(max_length=30)
    basic=models.IntegerField()
    pay_status=models.BooleanField(max_length=30)
    grade_pay=models.CharField(max_length=30)
    remark=models.CharField(max_length=30)
    #image and sign upload


class Salary(models.Model):
    Salary=models.IntegerField()
    #relation to employee_details model


#class Payslip(models.model):
