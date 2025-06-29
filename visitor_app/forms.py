from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser, VisitorRegistration
from django.forms.widgets import PasswordInput, TextInput

from django import forms


# Login Form
class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())


# Visitors registration form
class VisitorsForm(forms.ModelForm):
        class Meta:
                model = VisitorRegistration
                fields = ['full_name', 'phone_number', 'person_to_visit', 'visit_reason', 'hours_to_stay']
                labels = {
                'full_name': 'Full Name',
                'phone_number': 'Phone Number',
                'person_to_visit': 'Person to Visit',
                'visit_reason': 'Reason for Visit',
                'hours_to_stay': 'Duration of Stay (hours)',
                'visit_time': 'Visit Time'
                }

