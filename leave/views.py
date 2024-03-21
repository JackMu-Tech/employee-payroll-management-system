# leave/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest, LeaveType
from .forms import LeaveRequestForm, LeaveTypeForm

@login_required
def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user
            leave_request.save()
            return redirect('leave_request_success')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave/leave_request.html', {'form': form})

@login_required
def leave_request_success(request):
    return render(request, 'leave/leave_request_success.html')

@login_required
def leave_types(request):
    leave_types = LeaveType.objects.all()
    return render(request, 'leave/leave_types.html', {'leave_types': leave_types})

@login_required
def create_leave_type(request):
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave/leave_types')
    else:
        form = LeaveTypeForm()
    return render(request, 'leave/create_leave_type.html', {'form': form})
