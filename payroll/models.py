from django.db import models
from django.core.validators import FileExtensionValidator


class Employee_details(models.Model):
    #PERSONAL_DETAILSS
    id_no=models.PositiveIntegerField(unique =True, default=1)
    TITLE_CHOICES = [('', 'Select'),('1', 'Mr.'),('2', 'Mrs.'), ('3', 'Dr.')] 
    title=models.CharField(max_length=1,choices=TITLE_CHOICES,blank=False)
    first_name=models.CharField(max_length=30, default='')
    middle_name=models.CharField(max_length=30, default='')
    last_name=models.CharField(max_length=30, default='')
    date_of_birth = models.DateField()
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
    sequence_no=models.PositiveIntegerField(default=0)
    aadhar_id=models.CharField(max_length=20,default='')
    pan_no= models.CharField(max_length=20 , unique =True ,blank=False)
    email = models.EmailField(max_length=30,default='')
    mobile_no = models.CharField(max_length=20,default='')
    address=models.CharField(max_length=500,default='')
    # photo=models.FileField( default='')
    # sign=models.FileField(default='')
       
    # #SERVICE_DATE_DETAILS
    date_of_joining = models.DateField()
    date_of_relieving = models.DateField()
    date_of_increment = models.DateField()
    date_of_increment = models.DateField()
    date_of_retirement  = models.DateField()
    from_appointment_date = models.DateField()
    to_appointment_date = models.DateField()

    #SERVICE_TYEP_DETAILS


    # # #BASIC_DETAILS
    TA=models.BooleanField(blank=False)
    HRA=models.BooleanField(blank=False)
    handicap=models.BooleanField(blank=False)
    quarter=models.BooleanField(blank=False)
    senior_citizen=models.BooleanField(blank=False)
    
    QUARTER_TYPE_CHOICES = [  
        ('', 'Select'),
        ('1', 'CLASS 1'),
        ('2', 'CLASS 2'),
        ('3', 'CLASS 3'),
        ('4', 'CLASS 4'),
         ]
    quarter_type=models.CharField(max_length=1, choices=QUARTER_TYPE_CHOICES, blank=False)
    DESIGNATION_NATURE_CHOICES = [    
        ('', 'Select'),
        ('1', 'Permanent'),
        ('2', 'Permanent Teaching Non-Sanctioned'),
        ('3', 'Permanent Non-Teaching Excess'),
        ('4', 'Contractual Non-Teaching'),
        ('5', 'Contractual Teaching'),
            ]
    designation_nature=models.CharField(max_length=20, choices=DESIGNATION_NATURE_CHOICES,blank=False)

    DEPARTMENT_CHOICES = [  
        ('', 'Select'),
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
        ('', 'Select'),
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
        ('', 'Select'),
        ('0', 'Please Select'),    
        ('1', 'Regular'),
        ('2', 'DCPS'),
        ('3', 'Contractual NO EPF'),
        ('4', 'Contractual'),
        ('5', 'Contractual NT'),
           ]
    appointment=models.CharField(max_length=1, choices=APPOINTMENT_CHOICES,blank=False)
    STAFF_TYPE_CHOICES = [    
        ('', 'Select'),
        ('1', 'CLASS 1'),
        ('2', 'CLASS 2'),
        ('3', 'CLASS 3'),
        ('4', 'CLASS 4'),
        ('5', 'OTHER'),
        ('6', 'CONTRACTUAL'),
        ('7', 'CONTRACTUAL NT'),
        ]
    staff_type=models.CharField(max_length=1, choices=STAFF_TYPE_CHOICES, blank=False)
    

    # # #BASIC_DETAILS
    TA=models.BooleanField(blank=False)
    HRA=models.BooleanField(blank=False)
    handicap=models.BooleanField(blank=False)
    quarter=models.BooleanField(blank=False)
    senior_citizen=models.BooleanField(blank=False)
    
    QUARTER_TYPE_CHOICES = [  
        ('', 'Select'),
        ('1', 'CLASS 1'),
        ('2', 'CLASS 2'),
        ('3', 'CLASS 3'),
        ('4', 'CLASS 4'),
         ]
    quarter_type=models.CharField(max_length=1, choices=QUARTER_TYPE_CHOICES, blank=False)

    
    
    # # #BANK_DETAILS
    bank_acc_no= models.CharField(max_length=20,blank=False)
    ifsc_code =models.CharField(max_length=20,blank=False)
    BANK_NAME_CHOICES = [
        ('', 'Select'),
        ('0', 'Please Select'),    
        ('1', 'State Bank of India'),
        ('2', 'Bank Of Maharashtra'),  ]
    bank_name=models.CharField(max_length=1, choices=BANK_NAME_CHOICES, blank=False)
    bank_branch=models.CharField(max_length=30,blank=False)  
    epf=models.CharField(max_length=20,  blank=False)
    gpf_no = models.CharField(max_length=20, unique =True ,blank=False)
    dcps_no = models.CharField(max_length=20, unique =True ,blank=False)
    
    # # #PAY_SCALE_DETAILS
    RULE_CHOICES = [   
        ('', 'Select'),
        ('1', 'R7'),
        ('2', 'R6'),
        ('3', 'LUMSUM'),
        ('4', 'Daily Wages ')]
    rule=models.CharField(max_length=1, choices=RULE_CHOICES, blank=False)
    PAY_LEVEL_CHOICES = [
        ('', 'Select'),
        ('1', 'S-1(15000-47600)'),
        ('2', 'S-2(15300-48700)'),
        ('3', 'S-3(16600-52400)'),
        ('4', 'S-4(17100-54000)'),
        ('5', 'S-5(18000-56900)'),
        ('6', 'S-6(19900-63200)'),
        ('7', 'S-7(21700-69100)'),
        ('8', 'S-8(25500-81100)'),
        ('9', 'S-9(26400-83600)'),
        ('10', 'S-10(29200-92300)'),
        ('11', 'S-11(30100-95100)'),
        ('12', 'S-12(32000-101600)'),
        ('13', 'S-13(35400-112400)'),
        ('14', 'S-14(38600-122800)'),
        ('15', 'S-15(41800-132300)'),
        ('16', 'S-16(44900-142400)'),
        ('17', 'S-17(47600-151100)'),
        ('18', 'S-18(49100-155800)'),
        ('19', '1-1(0)'),
        ('20', '15600-39100(5000)'),
        ('21', '9A(56100-177500)'),
        ('22', '10(57700-182400)'),
        ('23', '11(68900-205500)'),
        ('24', '12(79800-211500)'),
        ('25', '13A1(131400-217100)'),
        ('26', '14(144200-218200)'),
        ('27','LUMSUM')]
    pay_level=models.CharField(max_length=30, choices=PAY_LEVEL_CHOICES, blank=False)
    CELL_NUMBER_CHOICES = [    
        ('', 'Select'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),]
    cell_number=models.CharField(max_length=10, choices=CELL_NUMBER_CHOICES, blank=False)
    basic=models.IntegerField(default=0)
    pay_status=models.BooleanField(blank=False)
    grade_pay=models.CharField(max_length=30,blank=False)

   
class Salary(models.Model):
    Salary=models.IntegerField()
    #relation to employee_details model

# class demo(models.Model):
#     sign=models.FileField(default='')
#class Payslip(models.model):
# class demo(models.Model):
#     id_no=models.PositiveIntegerField(unique =True, default=1000)
    

# class Payslip(models.model):
    
class staff_type(models.Model):
    stafftype =models.CharField(max_length=30, default='')



# retirement_age =models.CharField(max_length=10,default='')

class rule_man(models.Model):
    pay_rule =models.CharField(max_length=30, default='')
    rule_name =models.CharField(max_length=30, default='')
