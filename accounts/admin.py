from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User


class Admin(BaseAdmin):

    list_display = ['username', 'name', 'email', 'is_staff', 'is_active', 'date_joined']


admin.site.register(User, BaseAdmin)