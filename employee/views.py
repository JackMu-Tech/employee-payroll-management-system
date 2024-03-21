# employee/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Employee, TimeTracking
from .forms import EmployeeForm, TimeTrackingForm

def employee_list(request):
    employees = Employee.objects.all()

    # Pagination
    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'employee/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, 'Error adding employee. Please check the form.')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

def remove_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee removed successfully!')
        return redirect('employee_list')
    return render(request, 'employee/confirm_remove_employee.html', {'employee': employee})

def promote_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        # Logic to promote employee
        messages.success(request, 'Employee promoted successfully!')
        return redirect('employee_list')
    return render(request, 'employee/confirm_promote_employee.html', {'employee': employee})

@login_required
def record_hours(request):
    if request.method == 'POST':
        form = TimeTrackingForm(request.POST)
        if form.is_valid():
            time_tracking = form.save(commit=False)
            time_tracking.employee = request.user
            time_tracking.save()
            return redirect('employee/employee_list')  # Redirect to employee list or any other desired page
    else:
        form = TimeTrackingForm()
    return render(request, 'employee/record_hours.html', {'form': form})

@login_required
def edit_hours(request, time_tracking_id):
    time_tracking = TimeTracking.objects.get(pk=time_tracking_id)
    if request.method == 'POST':
        form = TimeTrackingForm(request.POST, instance=time_tracking)
        if form.is_valid():
            form.save()
            return redirect('employee/employee_list')  # Redirect to employee list or any other desired page
    else:
        form = TimeTrackingForm(instance=time_tracking)
    return render(request, 'employee/edit_hours.html', {'form': form})
