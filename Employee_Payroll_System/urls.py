# Employee_Payroll_System/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('login/', include('authentication.urls')),
    path('employee/', include('employee.urls')),
    path('payrol/', include('payrol.urls')),
    path('leave/', include('leave.urls')),
]
