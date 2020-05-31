from django.urls import path
from . import views
from register import views as register_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('activity/', views.activity, name='page-activity'),
    path('register/', register_view.register, name='page-register'),
    path('contact/', views.contact, name='page-contact'),
    path('appointment/', views.appointment, name='page-appointment'),
    path('profile/', register_view.profile, name='page-profile'),
    path('child/<str:pk>/', register_view.child, name='page-child'),
    path('create_child/<str:pk>/', register_view.addchild, name='add-child'),
    path('update_child/<str:pk>/', register_view.updateChild, name='update-child'),
    path('delete_child/<str:pk>/', register_view.deleteChild, name='delete-child')
]
