# employee/forms.py

from django import forms
from .models import Employee,TimeTracking

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position']

class TimeTrackingForm(forms.ModelForm):
    class Meta:
        model = TimeTracking
        fields = ['date', 'start_time', 'end_time']
