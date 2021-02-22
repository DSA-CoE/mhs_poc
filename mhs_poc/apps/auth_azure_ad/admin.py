from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from django.contrib.auth.models import Group
from .models import User


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        help_text='Change the password <a href="../password/">here</a>.'
    )

    class Meta:
        model = User
        fields = ()

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm

    # Inputs in the User edit page
    fieldsets = (
        (
            "Account",
            {"fields": ("username", "email", "password", "first_name", "last_name")},
        ),
        (
            "Permissions",
            {"fields": ("is_superuser", "is_staff", "is_active", "user_permissions")},
        ),
        (
            "Dates",
            {
                "fields": (
                    "account_expiry",
                    "date_joined",
                    "last_login",
                )
            },
        ),
        (
            "Token",
            {
                "fields": (
                    "access_token",
                    "id_token",
                    "token_expires",
                )
            },
        ),
    )


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
