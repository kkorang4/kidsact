from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, ChildForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        child_form = ChildForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid() and child_form.is_valid():
            users = user_form.save()
            profiles = profile_form.save()
            child_form.save()
            profiles.users = users

            profiles.save()
            return render(request, 'register/profile.html', {'users': users})
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        child_form = ChildForm(instance=request.user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'child_form': child_form
    }
    return render(request, 'register/profile.html', context)


