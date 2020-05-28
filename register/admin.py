from django.contrib import admin
from .models import Profile, Child


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')


class ChildAdmin(admin.ModelAdmin):
    list_display = ('user', 'child_name', 'child_age', 'notes')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Child, ChildAdmin)
