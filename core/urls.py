from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import CustomLoginView, DashboardView

app_name = 'core'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
