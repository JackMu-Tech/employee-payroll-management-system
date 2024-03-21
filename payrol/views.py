from django.shortcuts import render
from .models import Employee, Payroll

def payroll_summary(request):
    # Fetch payroll period from database or set it manually
    payroll_period = "January 2024"

    # Fetch all employees and their associated payroll information
    employees = Employee.objects.all()

    # Calculate deductions, net pay, and other payroll-related data for each employee
    for employee in employees:
        # Fetch payroll information for the current employee
        payroll = Payroll.objects.filter(employee=employee, period=payroll_period).first()

        # Perform calculations based on payroll data
        if payroll:
            # Example: Calculate total deductions (taxes, insurance, etc.)
            total_deductions = payroll.tax + payroll.insurance

            # Example: Calculate net pay (salary - deductions)
            net_pay = payroll.salary - total_deductions

            # Assign calculated values to the employee object
            employee.total_deductions = total_deductions
            employee.net_pay = net_pay
        else:
            # If no payroll information is found, set default values
            employee.total_deductions = 0
            employee.net_pay = 0

    context = {
        'payroll_period': payroll_period,
        'employees': employees,
    }
    return render(request, 'payrol/payroll_summary.html', context)

def dashboard(request):
    # Add your dashboard logic here
    return render(request, 'dashboard.html')

# Other views for payroll reports, settings, etc., can be added similarly
