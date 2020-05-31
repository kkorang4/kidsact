from django.contrib import admin
from .models import Activity, Appointment


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_age', 'price', 'staff', 'available')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child_name', 'act_name')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.site_header = 'BTC Admin'
