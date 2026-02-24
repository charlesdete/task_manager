from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Only include fields that exist on your custom User model
    list_display = ("id", "email_address", "first_name", "last_name", "is_staff", "is_superuser")
    search_fields = ("email_address", "first_name", "last_name")
    ordering = ("email_address",)

    # Remove references to groups and user_permissions
    filter_horizontal = ()
    list_filter = ("is_staff", "is_superuser", "department")  # adjust to your model fields
    fieldsets = (
        (None, {"fields": ("email_address", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number", "department")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email_address", "password1", "password2", "first_name", "last_name", "phone_number", "department"),
        }),
    )