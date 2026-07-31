from django.db import models
from attendance.models import Shift


class Holiday(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    holiday_date = models.DateField(blank=True, null=True)
    holiday_name = models.CharField(max_length=100, blank=True, null=True)
