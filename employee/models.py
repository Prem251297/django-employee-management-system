from django.db import models
from master.models import Department, Designation, Gender, SalaryMode, Bank


class Employee(models.Model):
    salutation = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(default='2000-01-01')
    joining_date = models.DateField(default='2000-01-01')
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    designation = models.ForeignKey(Designation, on_delete=models.RESTRICT)
    employment_type = models.CharField(max_length=20, choices=[('Permanent', 'Permanent'), ('Contract', 'Contract')], default='Permanent')
    gender = models.ForeignKey(Gender, on_delete=models.RESTRICT, blank=True, null=True)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, unique=True, blank=True, null=True)
    pan_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Left', 'Left')], default='Pending')
    current_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    salary_mode = models.ForeignKey(SalaryMode, on_delete=models.RESTRICT, blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.RESTRICT, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=11, blank=True, null=True)


    def __str__(self):
        return f"{self.salutation} {self.full_name}"

