from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Child
from django.core.validators import MaxValueValidator, MinValueValidator


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ['child_name', 'child_age', 'notes']