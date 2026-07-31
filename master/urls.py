from django.urls import path

from . import views

app_name = 'master'

urlpatterns = [
    # For Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/add/', views.DepartmentCreateView.as_view(), name='department_add'),
    path('departments/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_edit'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),

    # For Designation Category URLs
    path('designation-categories/', views.DesignationCategoryListView.as_view(), name='designation_category_list'),
    path('designation-categories/add/', views.DesignationCategoryCreateView.as_view(), name='designation_category_add'),
    path('designation-categories/<int:pk>/edit/', views.DesignationCategoryUpdateView.as_view(), name='designation_category_edit'),
    path('designation-categories/<int:pk>/delete/', views.DesignationCategoryDeleteView.as_view(), name='designation_category_delete'),

    # For Gender URLs
    path('genders/', views.GenderListView.as_view(), name='gender_list'),
    path('genders/add/', views.GenderCreateView.as_view(), name='gender_add'),
    path('genders/<int:pk>/edit/', views.GenderUpdateView.as_view(), name='gender_edit'),
    path('genders/<int:pk>/delete/', views.GenderDeleteView.as_view(), name='gender_delete'),

    # For Allowance URLs
    path('allowances/', views.AllowanceListView.as_view(), name='allowance_list'),
    path('allowances/add/', views.AllowanceCreateView.as_view(), name='allowance_add'),
    path('allowances/<int:pk>/edit/', views.AllowanceUpdateView.as_view(), name='allowance_edit'),
    path('allowances/<int:pk>/delete/', views.AllowanceDeleteView.as_view(), name='allowance_delete'),
]
