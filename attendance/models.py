from django.db import models
from employee.models import Employee
from master.models import Shift


class DutyRoster(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.full_name} - {self.shift.shift_name} on {self.date}"


class Attendance(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.DateTimeField(blank=True, null=True)
    check_out_time = models.DateTimeField(blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, blank=True, null=True)
    working_hours = models.DurationField(blank=True, null=True)
    is_late_entry = models.BooleanField(default=False)
    is_early_leave = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Leave', 'On Leave')], default='Absent')

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"