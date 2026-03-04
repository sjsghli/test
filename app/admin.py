from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Custom", {"fields": ("custom_field",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom", {"fields": ("custom_field",)}),
    )
    list_display = UserAdmin.list_display + ("custom_field",)


admin.site.register(User, CustomUserAdmin)
