from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # Add more fields for employee details as needed
    # Example: email = models.EmailField()
    # Example: date_of_birth = models.DateField()s

class TimeTracking(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.employee.username} - {self.date}"

    def __str__(self):
        return self.name
