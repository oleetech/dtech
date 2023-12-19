# attendance/urls.py
from django.urls import path
from .views import mark_in, mark_out, attendance_view,task_list, add_task

urlpatterns = [
    path('mark_in/', mark_in, name='mark_in'),
    path('mark_out/', mark_out, name='mark_out'),
    path('attendance/', attendance_view, name='attendance_view'),  # Add this line
    path('task_list/', task_list, name='task_list'),
    path('add_task/', add_task, name='add_task'),
]
