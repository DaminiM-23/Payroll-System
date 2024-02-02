from django.db import models


 

class Employee_details(models.Model):
    #PERSONAL_DETAILSS
    id_no=models.PositiveIntegerField(unique =True, default=1)
    TITLE_CHOICES = [('', 'Select'),('1', 'Mr.'),('2', 'Mrs.'), ('3', 'Dr.')] 
    id_no=models.PositiveIntegerField(unique =True, default=1)
    TITLE_CHOICES = [('', 'Select'),('1', 'Mr.'),('2', 'Mrs.'), ('3', 'Dr.')] 
    title=models.CharField(max_length=1,choices=TITLE_CHOICES,blank=False)
    first_name=models.CharField(max_length=30, default='')
    middle_name=models.CharField(max_length=30, default='')
    last_name=models.CharField(max_length=30, default='')
    date_of_birth = models.DateField()
    GENDER_CHOICES = [('', 'Select'),('M', 'Male'),('F', 'Female'), ('O', 'Other')] 
    GENDER_CHOICES = [('', 'Select'),('M', 'Male'),('F', 'Female'), ('O', 'Other')] 
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=False)
    EMPLOYEE_TYPE_CHOICES = [
        ('', 'Select'),
        ('1', 'Permanent'),
        # ('2', 'Permanent Teaching Non-Sanctioned'),
        # ('3', 'Permanent Non-Teaching Excess'),
        ('2', 'Contractual Non-Teaching'),
        ('3', 'Contractual Teaching'),
        ('4', 'Security'),
    ]
    employee_type=models.CharField(max_length=40, choices=EMPLOYEE_TYPE_CHOICES, blank=False)
    EMPLOYEE_TYPE_CHOICES = [
        ('', 'Select'),
        ('1', 'Permanent'),
        # ('2', 'Permanent Teaching Non-Sanctioned'),
        # ('3', 'Permanent Non-Teaching Excess'),
        ('2', 'Contractual Non-Teaching'),
        ('3', 'Contractual Teaching'),
        ('4', 'Security'),
    ]
    employee_type=models.CharField(max_length=40, choices=EMPLOYEE_TYPE_CHOICES, blank=False)
    sequence_no=models.PositiveIntegerField(default=0)
    aadhar_id=models.CharField(max_length=20,default='')
    pan_no= models.CharField(max_length=20 , unique =True ,blank=False)
    email = models.EmailField(max_length=30,default='')
    mobile_no = models.CharField(max_length=20,default='')
    address=models.CharField(max_length=500,default='')
    address=models.CharField(max_length=500,default='')
    # photo=models.FileField( default='')
    # sign=models.FileField(default='')
       
       
    # #SERVICE_DATE_DETAILS
    date_of_joining = models.DateField()
    date_of_relieving = models.DateField()
    date_of_increment = models.DateField()
    date_of_increment = models.DateField()
    date_of_increment = models.DateField()
    date_of_retirement  = models.DateField()
    from_appointment_date = models.DateField()
    to_appointment_date = models.DateField()
    # # #BASIC_DETAILS
    TA=models.BooleanField(blank=False)
    HRA=models.BooleanField(blank=False)
    handicap=models.BooleanField(blank=False)
    quarter=models.BooleanField(blank=False)
    senior_citizen=models.BooleanField(blank=False)
    designation_nature=models.CharField(max_length=20,blank=False),
    department=models.CharField(max_length=20, blank=False),
    designation=models.CharField(max_length=20,blank=False)
    appointment=models.CharField(max_length=20,blank=False)
    staff_type=models.CharField(max_length=20, blank=False)
    # # #BANK_DETAILS
    bank_acc_no= models.CharField(max_length=20,blank=False)
    ifsc_code =models.CharField(max_length=20,blank=False)
    bank=models.CharField(max_length=30, default='', blank=False)
    bank=models.CharField(max_length=30, default='', blank=False)
    bank_branch=models.CharField(max_length=30,blank=False)  
    epf=models.CharField(max_length=20,  blank=False)
    gpf_no = models.CharField(max_length=20, unique =True ,blank=False)
    dcps_no = models.CharField(max_length=20, unique =True ,blank=False)
    rule=models.CharField(max_length=10, blank=False)
    pay_level=models.CharField(max_length=30, blank=False)
    cell_number=models.CharField(max_length=10, blank=False)
    basic=models.IntegerField(default=0)
    pay_status=models.BooleanField(blank=False)
    grade_pay=models.CharField(max_length=30,blank=False)

    class Meta:
         verbose_name_plural="Employee Details"
    


class staff_type(models.Model):
    stafftype =models.CharField(max_length=30, default='')
    retirement_age =models.IntegerField(default='')

    class Meta:
         verbose_name_plural="staff"


class rule_man(models.Model):
    pay_rule =models.CharField(max_length=30, default='')
    rule_name =models.CharField(max_length=30, default='')

    class Meta:
         verbose_name_plural="Rule"

class PayLevelMaster(models.Model):
    staff_type=models.CharField(max_length=30, blank=False)
    pay_level=models.CharField(max_length=30, default='')   
    cell_1=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_2=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_3=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_4=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_5=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_6=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_7=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_8=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_9=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_10=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_11=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_12=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_13=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_14=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_15=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_16=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_17=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_18=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_19=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_20=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_21=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_22=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_23=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_24=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_25=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_26=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_27=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_28=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_29=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_30=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_31=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_32=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_33=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_34=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_35=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_36=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_37=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_38=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_39=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)
    cell_40=models.DecimalField(max_digits=20, decimal_places=5, default=0.0)

    def __str__(self):
        return f"{self.staff_type} - {self.pay_level}"

    
class department(models.Model):
    dep_name=models.CharField(max_length=30, default='', blank=False)

class designation(models.Model):
    designation=models.CharField(max_length=30, default='', blank=False)

class des_nature(models.Model):
    des_nature=models.CharField(max_length=100, default='', blank=False)

class appointment(models.Model):
    appointment=models.CharField(max_length=30, default='', blank=False)

class bank(models.Model):
    bank=models.CharField(max_length=30, default='', blank=False)


 
class payhead_earning(models.Model):
    pay_head=models.CharField( max_length=20, default='', blank=False)
    f_name=models.CharField( max_length=30, default='', blank=False)

    
class payment_head(models.Model):
    # Paycode=models.CharField( max_length=20, default='', blank=False)
    head=models.CharField( max_length=20, default='', blank=False)
    type_choices=[('','Select'),('1','Calculative'),('2','Earning')]
    type=models.CharField(choices=type_choices,max_length=20, default='', blank=False)
    cal=models.CharField( max_length=20, blank=False, default= "BASIC" )
    
class payhead_deduction(models.Model):
    pay_head=models.CharField( max_length=20, default='', blank=False)
    f_name=models.CharField( max_length=30, default='', blank=False)

class deduction_rule(models.Model):
    rule=models.CharField(max_length=30, default='', blank=False)
    cal=models.CharField(max_length=30, default='', blank=False)
    per=models.DecimalField( decimal_places=5,max_digits=10,default='', blank=False)
    head_deduction=models.CharField( max_length=20, default='', blank=False)
    eff_date=models.DateField(max_length=30, default='', blank=False)

    class Meta:
         verbose_name_plural="Deduction Rule"
         

class earning_rule(models.Model):
    rule=models.CharField(max_length=30, default='', blank=False)
    cal=models.CharField(max_length=30, default='', blank=False)
    per=models.DecimalField( decimal_places=5,max_digits=10,default='', blank=False)
    head_earning=models.CharField( max_length=20, default='', blank=False)
    eff_date=models.DateField(max_length=30, default='', blank=False)

    class Meta:
         verbose_name_plural="Earning Rule"