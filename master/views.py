from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import RestrictedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import DepartmentForm, DesignationCategoryForm, GenderForm, AllowanceForm
from .models import Department, DesignationCategory, Gender, Allowance


# For Department Views
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'master/department/list.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            queryset = queryset.filter(department__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'master/department/create.html'
    success_url = reverse_lazy('master:department_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Department created successfully.')
        return response


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'master/department/update.html'
    success_url = reverse_lazy('master:department_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Department updated successfully.')
        return response


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'master/department/delete.html'
    context_object_name = 'department'
    success_url = reverse_lazy('master:department_list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except RestrictedError:
            messages.error(
                self.request,
                'This department cannot be deleted because it is linked to existing employee records.',
            )
            return redirect('master:department_list')
        messages.success(self.request, 'Department deleted successfully.')
        return response


# For Designation Category Views
class DesignationCategoryListView(LoginRequiredMixin, ListView):
    model = DesignationCategory
    template_name = 'master/designation_category/list.html'
    context_object_name = 'designation_categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            queryset = queryset.filter(designation_category__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class DesignationCategoryCreateView(LoginRequiredMixin, CreateView):
    model = DesignationCategory
    form_class = DesignationCategoryForm
    template_name = 'master/designation_category/create.html'
    success_url = reverse_lazy('master:designation_category_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Designation category created successfully.')
        return response


class DesignationCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = DesignationCategory
    form_class = DesignationCategoryForm
    template_name = 'master/designation_category/update.html'
    success_url = reverse_lazy('master:designation_category_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Designation category updated successfully.')
        return response


class DesignationCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = DesignationCategory
    template_name = 'master/designation_category/delete.html'
    context_object_name = 'designation_category'
    success_url = reverse_lazy('master:designation_category_list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except RestrictedError:
            messages.error(
                self.request,
                'This designation category cannot be deleted because it is linked to existing employee records.',
            )
            return redirect('master:designation_category_list')
        messages.success(self.request, 'Designation category deleted successfully.')
        return response


# For Gender Views
class GenderListView(LoginRequiredMixin, ListView):
    model = Gender
    template_name = 'master/gender/list.html'
    context_object_name = 'genders'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            queryset = queryset.filter(gender__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class GenderCreateView(LoginRequiredMixin, CreateView):
    model = Gender
    form_class = GenderForm
    template_name = 'master/gender/create.html'
    success_url = reverse_lazy('master:gender_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Gender created successfully.')
        return response


class GenderUpdateView(LoginRequiredMixin, UpdateView):
    model = Gender
    form_class = GenderForm
    template_name = 'master/gender/update.html'
    success_url = reverse_lazy('master:gender_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Gender updated successfully.')
        return response


class GenderDeleteView(LoginRequiredMixin, DeleteView):
    model = Gender
    template_name = 'master/gender/delete.html'
    context_object_name = 'gender'
    success_url = reverse_lazy('master:gender_list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except RestrictedError:
            messages.error(
                self.request,
                'This gender cannot be deleted because it is linked to existing employee records.',
            )
            return redirect('master:gender_list')
        messages.success(self.request, 'Gender deleted successfully.')
        return response


# For Allowance Views
class AllowanceListView(LoginRequiredMixin, ListView):
    model = Allowance
    template_name = 'master/allowance/list.html'
    context_object_name = 'allowances'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            queryset = queryset.filter(allowance__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class AllowanceCreateView(LoginRequiredMixin, CreateView):
    model = Allowance
    form_class = AllowanceForm
    template_name = 'master/allowance/create.html'
    success_url = reverse_lazy('master:allowance_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Allowance created successfully.')
        return response


class AllowanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Allowance
    form_class = AllowanceForm
    template_name = 'master/allowance/update.html'
    success_url = reverse_lazy('master:allowance_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Allowance updated successfully.')
        return response


class AllowanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Allowance
    template_name = 'master/allowance/delete.html'
    context_object_name = 'allowance'
    success_url = reverse_lazy('master:allowance_list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except RestrictedError:
            messages.error(
                self.request,
                'This allowance cannot be deleted because it is linked to existing employee records.',
            )
            return redirect('master:allowance_list')
        messages.success(self.request, 'Allowance deleted successfully.')
        return response
