from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import CustomUser, VisitorRegistration

from .forms import LoginForm, VisitorsForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import logout

from datetime import date
from django.utils.timezone import localdate
from django.utils import timezone
from datetime import datetime


# Create your views here.


@login_required(login_url=reverse_lazy('login_page'))
def dashboard(request):
    today = timezone.localdate()

    start_datetime = timezone.make_aware(datetime.combine(today, datetime.min.time()))
    end_datetime = timezone.make_aware(datetime.combine(today, datetime.max.time()))

    records = VisitorRegistration.objects.all()
    todays_records = VisitorRegistration.objects.filter(
        check_in_date__range=(start_datetime, end_datetime)
    )

    context = {
        'records': records,
        'todays_records': todays_records,
        'today': today,
    }
    return render(request, 'visitor_app/dashboard.html', context)


def register_visitor(request):
    
    form = VisitorsForm()

    if request.method == "POST":
         form = VisitorsForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('after_registration')
         
    context = {'form':form}
    return render(request, 'visitor_app/register_visitor.html', context)


@login_required(login_url=reverse_lazy('login_page'))
def after_registration(request):
    return render(request, 'visitor_app/after_registration.html')


# Login function
def login_page(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)


            if user is not None:
                auth.login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url) if next_url else redirect('dashboard')


    context = {'form':form}

    return render(request, 'visitor_app/login_page.html', context)


# Logout Function
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login_page')