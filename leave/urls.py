from django.urls import path
from leave import views as leave_views

urlpatterns = [
    path('leave-request/', leave_views.leave_request, name='leave_request'),
    path('leave-request/success/', leave_views.leave_request_success, name='leave_request_success'),
    path('leave-types/', leave_views.leave_types, name='leave_types'),
    path('leave-types/create/', leave_views.create_leave_type, name='create_leave_type'),
]
