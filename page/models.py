from django.db import models
from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from register import models as pmodels
from django.core.validators import MaxValueValidator, MinValueValidator

TIME_CHOICE = [
        ('MORNING', '8am-12am'),
        ('AFTERNOON', '1pm-5pm')
    ]


class Activity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    min_age = models.IntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(13)])
    price = models.FloatField(default=0.00, validators=[MinValueValidator(0), MaxValueValidator(500)])
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(choices=TIME_CHOICE, default="MORNING", max_length=10)
    available = models.BooleanField(default=True)
    image_url = models.CharField(max_length=2083)
    date_open = models.DateField(default=timezone.now)
    max_capacity = models.IntegerField(default=12, validators=[MinValueValidator(6), MaxValueValidator(40)])

    def __str__(self):
        return f'{self.name}'


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    query = forms.CharField(widget=forms.Textarea, required=True)


class Appointment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parentR', null=True)
    child_name = models.ForeignKey(pmodels.Child, on_delete=models.CASCADE, default='', related_name='childR')
    activity_name = models.ForeignKey(Activity, to_field='name', db_column='name',
                                      on_delete=models.CASCADE, related_name='nameR', default='')
    activity_date = models.DateField(default=date.today)
    activity_time = models.CharField(choices=TIME_CHOICE, default='', max_length=10)
