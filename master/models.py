from django.db import models


class BaseMaster(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Department(BaseMaster):
    department = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["department"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.department


class DesignationCategory(BaseMaster):
    designation_category = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["designation_category"]
        verbose_name = "Designation Category"
        verbose_name_plural = "Designation Categories"

    def __str__(self):
        return self.designation_category


class Designation(BaseMaster):
    designation = models.CharField(max_length=100, unique=True)
    designation_category = models.ForeignKey(DesignationCategory, on_delete=models.RESTRICT, related_name="designations")

    class Meta:
        ordering = ["designation"]
        verbose_name = "Designation"
        verbose_name_plural = "Designations"

    def __str__(self):
        return f"{self.designation} ({self.designation_category})"

class Gender(BaseMaster):
    gender = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ["gender"]
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return self.gender


class SalaryMode(BaseMaster):
    salary_mode = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["salary_mode"]
        verbose_name = "Salary Mode"
        verbose_name_plural = "Salary Modes"

    def __str__(self):
        return self.salary_mode


class Bank(BaseMaster):
    bank = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["bank"]
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self):
        return self.bank


class Allowance(BaseMaster):
    allowance = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=20, unique=True, null=True, blank=True)

    class Meta:
        ordering = ["allowance"]
        verbose_name = "Allowance"
        verbose_name_plural = "Allowances"

    def __str__(self):
        return self.allowance


class Deduction(BaseMaster):
    deduction = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=20, unique=True, null=True, blank=True)

    class Meta:
        ordering = ["deduction"]
        verbose_name = "Deduction"
        verbose_name_plural = "Deductions"

    def __str__(self):
        return self.deduction


class Shift(BaseMaster):
    shift = models.CharField(max_length=50, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    grace_period = models.IntegerField(default=0, help_text="Grace period in minutes")
    is_night_shift = models.BooleanField(default=False)

    class Meta:
        ordering = ["shift"]
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"

    def __str__(self):
        return self.shift


class Country(BaseMaster):
    country = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["country"]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country


class State(BaseMaster):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT, related_name="states")
    state = models.CharField(max_length=100)

    class Meta:
        ordering = ["state"]
        verbose_name = "State"
        verbose_name_plural = "States"
        constraints = [
            models.UniqueConstraint(
                fields=["country", "state"],
                name="unique_country_state"
            )
        ]

    def __str__(self):
        return self.state


class City(BaseMaster):
    state = models.ForeignKey(State, on_delete=models.RESTRICT, related_name="cities")
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ["city"]
        verbose_name = "City"
        verbose_name_plural = "Cities"
        constraints = [
            models.UniqueConstraint(
                fields=["state", "city"],
                name="unique_state_city"
            )
        ]

    def __str__(self):
        return self.city