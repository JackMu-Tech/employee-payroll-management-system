# employee/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('remove/<int:employee_id>/', views.remove_employee, name='remove_employee'),
    path('promote/<int:employee_id>/', views.promote_employee, name='promote_employee'),
    path('record-hours/', views.record_hours, name='record_hours'),
    path('edit-hours/<int:time_tracking_id>/', views.edit_hours, name='edit_hours'),
]
