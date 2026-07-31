from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from core.forms import LoginForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        if not self.request.POST.get('remember_me'):
            self.request.session.set_expiry(0)
        return response


class DashboardView(LoginRequiredMixin, TemplateView):
    """Renders the HRMS dashboard shell with placeholder data.

    Stats, recent employees, and activities are hardcoded for now since
    the Employee/Attendance/Leave modules aren't wired up yet — swap these
    for real querysets once those apps have data and views.
    """
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = [
            {'label': 'Total Employees', 'value': 128, 'icon': 'bi-people-fill', 'color': 'primary'},
            {'label': 'Departments', 'value': 8, 'icon': 'bi-diagram-3-fill', 'color': 'success'},
            {'label': 'Active Employees', 'value': 121, 'icon': 'bi-person-check-fill', 'color': 'info'},
            {'label': "Today's Attendance", 'value': '96%', 'icon': 'bi-calendar-check-fill', 'color': 'warning'},
        ]
        context['recent_employees'] = [
            {'name': 'Ananya Sharma', 'department': 'Human Resources', 'designation': 'HR Executive', 'joining_date': '2026-06-12', 'status': 'Active', 'status_color': 'success'},
            {'name': 'Rahul Verma', 'department': 'Engineering', 'designation': 'Software Engineer', 'joining_date': '2026-05-28', 'status': 'Active', 'status_color': 'success'},
            {'name': 'Priya Nair', 'department': 'Finance', 'designation': 'Accountant', 'joining_date': '2026-04-15', 'status': 'Pending', 'status_color': 'secondary'},
            {'name': 'Karthik Iyer', 'department': 'Sales', 'designation': 'Sales Manager', 'joining_date': '2026-03-02', 'status': 'Active', 'status_color': 'success'},
            {'name': 'Sneha Reddy', 'department': 'Engineering', 'designation': 'QA Analyst', 'joining_date': '2026-01-20', 'status': 'Active', 'status_color': 'success'},
        ]
        context['quick_actions'] = [
            {'label': 'Add Employee', 'icon': 'bi-person-plus'},
            {'label': 'Mark Attendance', 'icon': 'bi-calendar-check'},
            {'label': 'Apply Leave', 'icon': 'bi-file-earmark-plus'},
            {'label': 'Generate Payroll', 'icon': 'bi-cash-stack'},
        ]
        context['recent_activities'] = [
            {'timestamp': 'Today, 09:42 AM', 'description': 'Rahul Verma checked in.'},
            {'timestamp': 'Today, 09:15 AM', 'description': 'Leave request from Priya Nair is pending approval.'},
            {'timestamp': 'Yesterday, 06:05 PM', 'description': 'Payroll processed for June 2026.'},
            {'timestamp': 'Yesterday, 11:20 AM', 'description': 'New employee Sneha Reddy onboarded.'},
        ]
        return context
