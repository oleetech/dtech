from django.shortcuts import render

# attendance/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Attendance
import datetime


@login_required
def attendance_view(request):
    return render(request, 'attendance/attendance_template.html')


@login_required
def mark_in(request):
    if request.method == 'POST':
        user = request.user
        date_today = datetime.date.today()
        intime = datetime.datetime.now().time()
        status = 'P'

        # TODO: Get latitude and longitude from Google Maps API

        Attendance.objects.create(user=user, date=date_today, intime=intime, status=status)
        return JsonResponse({'status': 'success'})

@login_required
def mark_out(request):
    if request.method == 'POST':
        user = request.user
        date_today = datetime.date.today()
        outtime = datetime.datetime.now().time()

        # TODO: Get latitude and longitude from Google Maps API

        attendance = Attendance.objects.filter(user=user, date=date_today).first()
        if attendance:
            attendance.outtime = outtime
            attendance.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No attendance record found'})





from .models import Task
from datetime import datetime

@login_required
def task_list(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    return render(request, 'task/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        user = request.user
        date = datetime.now().date()
        time_slot_1 = request.POST.get('time_slot_1', '')
        time_slot_2 = request.POST.get('time_slot_2', '')
        time_slot_3 = request.POST.get('time_slot_3', '')
        time_slot_4 = request.POST.get('time_slot_4', '')

        Task.objects.create(
            user=user,
            date=date,
            time_slot_1=time_slot_1,
            time_slot_2=time_slot_2,
            time_slot_3=time_slot_3,
            time_slot_4=time_slot_4
        )
        return redirect('task_list')

    return render(request, 'task/add_task.html')