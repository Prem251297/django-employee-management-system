from django.db import models

class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.leave_type


class leaveBalance(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=1, default=0.00)

    class Meta:
        unique_together = ('employee', 'leave_type')

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type.leave_type}: {self.balance}"


class LeaveRequest(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    leave_cancel_reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type.leave_type} from {self.start_date} to {self.end_date} ({self.status})"
