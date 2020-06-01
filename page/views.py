from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import AppointmentForm
from register import models as rModel
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, 'page/home.html')


def about(request):
    return render(request, 'page/about.html')


def activity(request):
    activities = Activity.objects.all()
    return render(request, 'page/activity.html', {'activities': activities})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            query = form.cleaned_data['query']
            email = request.user.email
            try:
                send_mail('email from ' + name,
                          query,
                          email,
                          [settings.EMAIL_HOST_USER],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'page/contact.html', {'name': name})
    return render(request, 'page/contact.html', {'form': form})


@login_required
def appointment(request, pk):
    appForm = AppointmentForm(request.POST)
    appForm.fields["parent"].queryset = User.objects.filter(id=pk)
    appForm.fields["child_name"].queryset = rModel.Child.objects.filter(parent=pk)
    appForm.fields["activity_name"].queryset = Activity.objects.filter(available=True)
    if request.method == 'POST':
        appForm = AppointmentForm(request.POST)
        appForm.fields["parent"].queryset = User.objects.filter(id=pk)
        appForm.fields["child_name"].queryset = rModel.Child.objects.filter(parent=pk)
        appForm.fields["activity_name"].queryset = Activity.objects.filter(available=True)
        if appForm.is_valid():
            apps = appForm.save()
            apps.save()

            template = render_to_string('page/email.html',
                                        {'name': request.user.first_name,
                                         'child_name': appForm.cleaned_data['child_name'],
                                         'activity_name': appForm.cleaned_data['activity_name'],
                                         'activity_date': appForm.cleaned_data['activity_date'],
                                         'activity_time': appForm.cleaned_data['activity_time']}
                                        )
            email = EmailMessage(
                'Thanks for booking the activity! BTC Activity',
                template,
                settings.EMAIL_HOST_USER,
                [request.user.email],
            )
            email.fail_silently = False
            email.send()
            return redirect('/activity/')
    context = {
        'appForm': appForm
    }
    return render(request, 'page/appointment.html', context)
