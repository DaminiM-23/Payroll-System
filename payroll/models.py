from django.db import models
#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
#from django.http import FileResponse
#from io import BytesIO

class User_login(models.Model):
    user_name=models.CharField(max_length=30)



class Employee_details(models.Model):
    #PERSONAL_DETAILS
    title=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30,null=False)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender=models.CharField(max_length=30)
    jntu_no=models.CharField(max_length=30)
    acite_id=models.CharField(max_length=30)
    employee_no=models.IntegerField()
    aadhar_or_unique_id=models.IntegerField()
    email = models.EmailField(max_length=30,unique=True)
    cell_no = models.IntegerField()
    Bloodgroup=models.CharField(max_length=10)
    #SERVICE_DATE_DETAILS
    date_of_joining=models.DateField()
    date_of_relieving = models.DateField()
    ate_of_increment = models.DateField()
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
    appoint_in=models.CharField(max_length=30)
    #BASIC_DETAILS
    TA=models.BooleanField(default=True)
    handicap=models.BooleanField(default=False)
    quarter=models.BooleanField(default=False)
    senior_citizen=models.BooleanField(default=False)
    quater_rent=models.BooleanField(default=False)
    quarter_type=models.CharField(max_length=30)
    #BANK_DETAILS
    bank_acc_no = models.IntegerField()
    ifsc_code = models.IntegerField()
    epf = models.IntegerField()
    ppf_no = models.IntegerField()
    pf_no = models.IntegerField()
    pan_no= models.IntegerField()
    #PAY_SCALE_DETAILS
    rule=models.CharField(max_length=30)
    scale=models.CharField(max_length=30)
    pay_level=models.CharField(max_length=30)
    cell_number=models.CharField(max_length=30)
    basic=models.IntegerField()
    pay_status=models.BooleanField(max_length=30)
    grade_pay=models.CharField(max_length=30)
    remark=models.CharField(max_length=30)


class Salary(models.Model):
    salary=models.IntegerField()
    #relation to employee_details model








#class Payslip(models.Model):
#    def generate_pdf(self):
#       buffer = BytesIO()
#       p = canvas.Canvas(buffer, pagesize=letter)
#       p.drawString(100, 750, f"Payslip for {self.employee} - {self.payroll_period}")
#       p.drawString(100, 700, f"Gross Pay: ${self.gross_pay}")
#        p.drawString(100, 680, f"Deductions: ${self.deductions}")
#        p.drawString(100, 660, f"Net Pay: ${self.net_pay}")
        # You can add more details as needed
#        p.showPage()
#        p.save()
#        buffer.seek(0)
#        return FileResponse(buffer, as_attachment=True, filename=f'payslip_{self.id}.pdf')

    












    
    



    
