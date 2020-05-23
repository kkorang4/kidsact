from django.contrib import admin
from .models import Activity, Appointment


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_age', 'price', 'staff', 'available')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Appointment)
