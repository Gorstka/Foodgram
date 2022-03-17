from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    list_display = ("pk", "username", "email")
    list_filter = BaseUserAdmin.list_filter + ("email", "username")
    search_fields = ["username", "email"]


admin.site.register(CustomUser, CustomUserAdmin)
