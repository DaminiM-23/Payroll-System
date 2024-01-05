from django.db import models


class Employee_details(models.Model):
    #PERSONAL_DETAILSS
    id_no=models.PositiveIntegerField(unique =True, default=1000)
    title=models.CharField(max_length=30, default='')
    first_name=models.CharField(max_length=30, default='')
    middle_name=models.CharField(max_length=30, default='')
    last_name=models.CharField(max_length=30, default='')
    father_name=models.CharField(max_length=30, default='')
    date_of_birth = models.DateField()
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'), ('O', 'Other'),] 
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=False)
    jntu_no=models.CharField(max_length=30 ,unique=True,default='')
    acite_id=models.CharField(max_length=30 ,unique=True,default='')
    employee_no=models.CharField(max_length=30,default='')
    sequence_no=models.PositiveIntegerField(default=0)
    aadhar_id=models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=30,default='')
    cell_no = models.CharField(max_length=20,default='')
    BLOOD_GROUP_CHOICES = [
        ('1', 'A+ve'),
        ('2', 'A-ve'),
        ('3', 'B+ve'),
        ('4', 'B-ve'),
        ('5', 'AB+ve'),
        ('6', 'AB-ve'),
        ('7', 'O+ve'),
        ('8', 'O-ve'),
        ('9', 'Other'),]
    bloodgroup=models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES,blank=False)
    # photo=models.FileField( default='')
    # sign=models.FileField(default='')

    # #SERVICE_DATE_DETAILS
    date_of_joining = models.DateField()
    SHIFT_CHOICES = [('forenoon', 'Forenoon'), ('afternoon', 'Afternoon')]
    shift_joining=models.CharField(max_length=10, choices=SHIFT_CHOICES,blank=False)
    date_of_relieving = models.DateField()
    shift_relieving=models.CharField(max_length=10, choices=SHIFT_CHOICES,blank=False)
    date_of_increment = models.DateField()
    pay_revised_date  = models.DateField()
    date_of_retirement  = models.DateField()
    from_appointment_date = models.DateField()
    to_appointment_date = models.DateField()

    #SERVICE_TYEP_DETAILS
    DESIGNATION_NATURE_CHOICES = [    
        ('1', 'Permanent'),
        ('2', 'Permanent Teaching Non-Sanctioned'),
        ('3', 'Permanent Non-Teaching Excess'),
        ('4', 'Contractual Non-Teaching'),
        ('5', 'Contractual Teaching'),
        ('6', 'PG'),
            ]
    designation_nature=models.CharField(max_length=20, choices=DESIGNATION_NATURE_CHOICES,blank=False)

    DEPARTMENT_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'ACCOUNTS'),
        ('2', 'ADMIN'),
        ('3', 'CHEMISTRY'),
        ('4', 'CIVIL'),
        ('5', 'COMPUTER'),
        ('6', 'ELECTRONICS COMPUTER'),
        ('7', 'ELECTRICAL'),
        ('8', 'ESTABLISHMENT'),
        ('9', 'EXAM'),
        ('10', 'HOSTEL'),
        ('11', 'HUMANITIES'),
        ('12', 'LIBRARY'),
        ('13', 'MAINTENANCE'),
        ('14', 'MATHS'),
        ('15', 'MCA'),
        ('16', 'MECHANICAL'),
        ('17', 'PHYSICS'),
        ('18', 'PRODUCTION'),
        ('19', 'STRUCTURAL'),
        ('20', 'TEXTILE'),
        ('21', 'GYMKHANA'),
        ('22', 'STORE'),
        ('23', 'W/M SECURITY'),
        ('24', 'TPO'),
        ]
    department=models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=False)
    DESIGNATION_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'Professor'),
        ('2', 'Training and Placement Officer'),
        ('3', 'Junior Engineer'),
        ('4', 'System Manager'),
        ('5', 'CA'),
        ('6', 'Instructor'),
        ('7', 'Junior Clerk'),
        ('8', 'Junior Lab Assistant'),
        ('9', 'Lab Assistant'),
        ('10', 'Lab Attendant'),
        ('11', 'Lecturer'),
        ('12', 'Lib Attendant'),
        ('13', 'Library Clerk'),
        ('14', 'Mali'),
        ('15', 'Med Officer'),
        ('16', 'M Supervisor'),
        ('17', 'OSD'),
        ('18', 'Others'),
        ('19', 'Peon'),
        ('20', 'Senior Clerk'),
        ('21', 'Head Clerk'),
        ('22', 'Foreman'),
        ('23', 'Carpenter'),
        ('24', 'Adjunct faculty'),
        ('25', 'Adhoc faculty'),
        ('26', 'Tenure faculty'),
        ('27', 'Driver'),
        ('28', 'Assistant Professor'),
        ('29', 'Director'),
        ('30', 'STENO (M)'),
        ('31', 'D O'),
        ('32', 'Superintendent'),
        ('33', 'Assistant Instructor'),
        ('34', 'Accounts Officer'),
        ('35', 'System Engineer'),
        ('36', 'Office Assistant'),
        ('37', 'Watch Man'),
        ('38', 'Watch Man'),
        ('39', 'Hamal'),
        ('40', 'Sweeper'),
        ('41', 'Electrician'),
        ('42', 'Plumber'),
        ('43', 'System Analyst'),]
    designation=models.CharField(max_length=20, choices=DESIGNATION_CHOICES,blank=False)
    APPOINTMENT_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'Regular'),
        ('2', 'DCPS'),
        ('3', 'Contractual NO EPF'),
        ('4', 'Contractual'),
        ('5', 'Contractual NT'),
           ]
    appointment=models.CharField(max_length=1, choices=APPOINTMENT_CHOICES,blank=False)
    STAFF_TYPE_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'CLASS 1'),
        ('2', 'CLASS 2'),
        ('3', 'CLASS 3'),
        ('4', 'CLASS 4'),
        ('5', 'OTHER'),
        ('6', 'CONTRACTUAL'),
        ('7', 'CONTRACTUAL NT'),
        ]
    staff_type=models.CharField(max_length=1, choices=STAFF_TYPE_CHOICES, blank=False)
    BANK_NAME_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'State Bank of India'),
        ('2', 'Bank Of Maharashtra'),  ]
    bank_name=models.CharField(max_length=1, choices=BANK_NAME_CHOICES, blank=False)
    VOCATIONAL_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'Vacational'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),]
    vocational=models.CharField(max_length=1, choices=VOCATIONAL_CHOICES, blank=False)
    bank_branch=models.CharField(max_length=30,blank=False)
    USER_TYPE_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'Faculty'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ]
    user_type=models.CharField(max_length=1, choices=USER_TYPE_CHOICES, blank=False)
    APPOINTED_IN_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'Diploma'),
        ('2', 'Degree'),
        ('3', 'PG'),
        ('4', 'MCA'),
        ('5', 'Hostel'),
        ('6', 'Non-Teaching'),
        ('7', 'MCA Non-Teaching'),]
    appointed_in=models.CharField(max_length=1, choices=APPOINTED_IN_CHOICES, blank=False)

    # # #BASIC_DETAILS
    TA=models.BooleanField(blank=False)
    handicap=models.BooleanField(blank=False)
    quarter=models.BooleanField(blank=False)
    senior_citizen=models.BooleanField(blank=False)
    quarter_rent=models.BooleanField(blank=False)
    QUARTER_TYPE_CHOICES = [  
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
         ]
    quarter_type=models.CharField(max_length=1, choices=QUARTER_TYPE_CHOICES, blank=False)

    # # #BANK_DETAILS
    bank_acc_no= models.CharField(max_length=20,blank=False)
    ifsc_code =models.CharField(max_length=20,blank=False)
    EPF_CHOICES = [
        ('0', 'Please Select'),    
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),]
    epf=models.CharField(max_length=1, choices=EPF_CHOICES, blank=False)
    ppf_no = models.CharField(max_length=20, unique =True ,blank=False)
    pf_no = models.CharField(max_length=20, unique =True ,blank=False)
    pan_no= models.CharField(max_length=20 , unique =True ,blank=False)

    # # #PAY_SCALE_DETAILS
    RULE_CHOICES = [
        ('0', 'Please Select'),    
        ('1', 'R7'),
        ('2', 'R6'),
        ('3', 'CON'),]
    rule=models.CharField(max_length=1, choices=RULE_CHOICES, blank=False)
    SCALE_CHOICES = [
        ('0', 'Please Select'),    
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),]
    scale=models.CharField(max_length=1, choices=SCALE_CHOICES, blank=False)
    PAY_LEVEL_CHOICES = [
        ('0', 'Please Select'),    
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),]
    pay_level=models.CharField(max_length=1, choices=PAY_LEVEL_CHOICES, blank=False)
    CELL_NUMBER_CHOICES = [
        ('0', 'Please Select'),    
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),]
    cell_number=models.CharField(max_length=1, choices=CELL_NUMBER_CHOICES, blank=False)
    basic=models.IntegerField(default=0)
    pay_status=models.BooleanField(blank=False)
    grade_pay=models.CharField(max_length=30,blank=False)
    remark=models.CharField(max_length=30,blank=False)
   


class Salary(models.Model):
    Salary=models.IntegerField()
    #relation to employee_details model

# class demo(models.Model):
#     sign=models.FileField(default='')
#class Payslip(models.model):
