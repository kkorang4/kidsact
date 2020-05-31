from django import forms
from django.contrib.auth.models import User
from .models import Activity, Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['child_name', 'act_name', 'act_date', 'act_time']
