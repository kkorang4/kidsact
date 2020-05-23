from django import forms
from django.contrib.auth.models import User
from .models import Activity, Appointment


class AppointmentForm(forms.ModelForm):
    activity_name = forms.CharField()
    a_date = forms.DateField()
    child_name = forms.CharField()
    child_age = forms.IntegerField()

    class Meta:
        model = Appointment
        fields = ['activity_name', 'a_date', 'child_name', 'child_age']
