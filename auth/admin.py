from django.contrib.auth.admin import UserAdmin
from auth.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','public_key', 'site_manager')

admin.site.register(UserProfile, UserProfileAdmin)