from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from register import models as pmodels
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Activity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    min_age = models.IntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(13)])
    price = models.FloatField(default=0.00, validators=[MinValueValidator(0), MaxValueValidator(500)])
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    image_url = models.CharField(max_length=2083)
    date_open = models.DateField(default=timezone.now)
    max_capacity = models.IntegerField(default=12, validators=[MinValueValidator(6), MaxValueValidator(40)])


class ContactForm(forms.Form):
    email_address = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    query = forms.CharField(widget=forms.Textarea, required=True)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(pmodels.Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Appointment'
