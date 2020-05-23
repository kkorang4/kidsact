from django.urls import path
from . import views
from register import views as register_view

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('activity/', views.activity, name='page-activity'),
    path('register/', register_view.register, name='page-register'),
    path('contact/', views.contact, name='page-contact'),
    path('appointment/', views.appointment, name='page-appointment')
]
