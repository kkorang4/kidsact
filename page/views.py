from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Activity, ContactForm
from .forms import AppointmentForm


def home(request):
    activities = Activity.objects.all()
    return render(request, 'page/home.html', {'activities': activities})


def about(request):
    return render(request, 'page/about.html')


def activity(request):
    activities = Activity.objects.all()
    return render(request, 'page/activity.html', {'activities': activities})


def contact(request, send_to="kima11@myunitec.ac.nz"):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            name = form.cleaned_data['name']
            query = form.cleaned_data['query']
            try:
                send_mail('email from ' + name,
                          query,
                          email_address,
                          [send_to],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'page/contact.html', {'name': name})
    return render(request, 'page/contact.html', {'form': form})


@login_required
def appointment(request):
    appForm = AppointmentForm()
    context = {
        'appForm': appForm
    }
    return render(request, 'page/appointment.html', context)
