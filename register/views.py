from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, ChildForm
from .models import *


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
        if user_form.is_valid() and profile_form.is_valid():
            users = user_form.save()
            profiles = profile_form.save()

            profiles.users = users
            profiles.save()

            return render(request, 'register/profile.html', {'users': users})
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'register/profile.html', context)


@login_required()
def child(request, pk):
    ChildFormSet = inlineformset_factory(User, Child, fields=('child_name', 'child_age', 'notes'), extra=1)
    parent = User.objects.get(id=pk)
    children = parent.children.all()
    formset = ChildFormSet(queryset=Child.objects.none(), instance=parent)
    if request.method == 'POST':
        print('PRINTING POST:', request.POST)
        child_form = ChildForm(request.POST)
        formset = ChildFormSet(request.POST, instance=parent)
        if child_form.is_valid():
            formset.save()
            return redirect('/profile/')
    context = {'child_form': formset,
               'children': children}
    return render(request, 'register/child.html', context)


@login_required()
def addchild(request, pk):
    ChildFormSet = inlineformset_factory(User, Child, fields=('child_name', 'child_age', 'notes')
                                         , extra=1, can_delete=False)
    parent = User.objects.get(id=pk)
    children = parent.children.all()
    formset = ChildFormSet(queryset=Child.objects.none(), instance=parent)
    if request.method == 'POST':
        child_form = ChildForm(request.POST)
        formset = ChildFormSet(request.POST, instance=parent)
        if child_form.is_valid():
            formset.save()
            return redirect('/profile/')
    context = {'child_form': formset,
               'children': children}
    return render(request, 'register/childform.html', context)


@login_required()
def updateChild(request, pk):
    children = Child.objects.get(id=pk)
    child_form = ChildForm(instance=children)
    if request.method == 'POST':
        child_form = ChildForm(request.POST, instance=children)
        if child_form.is_valid():
            child_form.save()
            return redirect('/profile/')
    context = {'child_form': child_form}
    return render(request, 'register/childform.html', context)


@login_required()
def deleteChild(request, pk):
    children = Child.objects.get(id=pk)
    if request.method == 'POST':
        children.delete()
        return redirect('/profile/')
    context = {'child': children}
    return render(request, 'register/delete.html', context)
