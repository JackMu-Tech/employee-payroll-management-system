# payroll/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # Add more fields for employee details as needed

    def __str__(self):
        return self.name

class Payroll(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    period = models.CharField(max_length=100)  # e.g., "January 2024"
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    insurance = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields for payroll details as needed

    def __str__(self):
        return f"{self.employee.name}'s Payroll for {self.period}"
