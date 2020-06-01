from django import forms
from django.contrib.auth.models import User
from .models import *
from register import models as rModel


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['parent', 'child_name', 'activity_name', 'activity_date', 'activity_time']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['activity_name'].queryset = Activity.objects.filter(available=True)
