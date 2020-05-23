from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'child_name', 'child_age')


admin.site.register(Profile, ProfileAdmin)
