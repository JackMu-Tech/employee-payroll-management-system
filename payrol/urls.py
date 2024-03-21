# payroll/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.payroll_summary, name='payroll_summary'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Add URLs for other views here
]
