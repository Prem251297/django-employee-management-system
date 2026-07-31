from django import forms

from .models import Department, DesignationCategory, Gender, Allowance


class BootstrapModelForm(forms.ModelForm):
    """Base ModelForm that applies Bootstrap 5 field classes automatically.

    Shared by every master-data form so field styling isn't repeated
    per model across the ~12 master tables.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.setdefault('class', 'form-check-input')
            else:
                field.widget.attrs.setdefault('class', 'form-control')


class DepartmentForm(BootstrapModelForm):
    class Meta:
        model = Department
        fields = ['department', 'is_active']
        labels = {
            'department': 'Department Name',
            'is_active': 'Active',
        }
        widgets = {
            'department': forms.TextInput(attrs={'placeholder': 'e.g. Human Resources'}),
        }

    def clean_department(self):
        department = self.cleaned_data['department'].strip()
        duplicate = Department.objects.filter(department__iexact=department)
        if self.instance.pk:
            duplicate = duplicate.exclude(pk=self.instance.pk)
        if duplicate.exists():
            raise forms.ValidationError('A department with this name already exists.')
        return department


class DesignationCategoryForm(BootstrapModelForm):
    class Meta:
        model = DesignationCategory
        fields = ['designation_category', 'is_active']
        labels = {
            'designation_category': 'Designation Category Name',
            'is_active': 'Active',
        }
        widgets = {
            'designation_category': forms.TextInput(attrs={'placeholder': 'e.g. Teaching Staff'}),
        }

    def clean_designation_category(self):
        designation_category = self.cleaned_data['designation_category'].strip()
        duplicate = DesignationCategory.objects.filter(designation_category__iexact=designation_category)
        if self.instance.pk:
            duplicate = duplicate.exclude(pk=self.instance.pk)
        if duplicate.exists():
            raise forms.ValidationError('A designation category with this name already exists.')
        return designation_category


class GenderForm(BootstrapModelForm):
    class Meta:
        model = Gender
        fields = ['gender', 'is_active']
        labels = {
            'gender': 'Gender',
            'is_active': 'Active',
        }
        widgets = {
            'gender': forms.TextInput(attrs={'placeholder': 'e.g. Male'}),
        }

    def clean_gender(self):
        gender = self.cleaned_data['gender'].strip()
        duplicate = Gender.objects.filter(gender__iexact=gender)
        if self.instance.pk:
            duplicate = duplicate.exclude(pk=self.instance.pk)
        if duplicate.exists():
            raise forms.ValidationError('A gender with this name already exists.')
        return gender


class AllowanceForm(BootstrapModelForm):
    class Meta:
        model = Allowance
        fields = ['allowance', 'short_name', 'is_active']
        labels = {
            'allowance': 'Allowance Name',
            'short_name': 'Short Name',
            'is_active': 'Active',
        }
        widgets = {
            'allowance': forms.TextInput(attrs={'placeholder': 'e.g. Housing Rent Allowance'}),
            'short_name': forms.TextInput(attrs={'placeholder': 'e.g. HRA'}),
        }

    def clean_allowance(self):
        allowance = self.cleaned_data['allowance'].strip()
        duplicate = Allowance.objects.filter(allowance__iexact=allowance)
        if self.instance.pk:
            duplicate = duplicate.exclude(pk=self.instance.pk)
        if duplicate.exists():
            raise forms.ValidationError('An allowance with this name already exists.')
        return allowance