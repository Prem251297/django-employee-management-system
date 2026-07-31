from django.db import models
from master.models import Allowance, Deduction

class EmployeeAllowance(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.RESTRICT)
    allowance = models.ForeignKey(Allowance, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('employee', 'allowance')


class EmployeeDeduction(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.RESTRICT)
    deduction = models.ForeignKey(Deduction, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('employee', 'deduction')