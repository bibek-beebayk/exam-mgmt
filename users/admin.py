from django.contrib import admin
from .models import User, Interest
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = [
        ("Authentication", {
            "fields": [
                "username",
                "password",
                "is_active",
                "is_staff",
                "is_superuser"
            ]
        }),
        ("Basic Info", {
            "fields": [
                "first_name",
                "middle_name",
                "last_name",
                "email",
                "address",
                "phone",
                "date_of_birth",
                "is_student",
                "date_joined"
            ]
        }),
        ("Permissions", {
            "fields": [
                "groups",
                "user_permissions"
            ]
        })
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    # form = UserChangeForm
    # add_form = UserCreationForm
    # change_password_form = AdminPasswordChangeForm
    # list_display = ("username", "email", "first_name", "last_name", "is_staff")
    # list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    # search_fields = ("username", "first_name", "last_name", "email")
    # ordering = ("username",)
    # filter_horizontal = (
    #     "groups",
    #     "user_permissions",
    # )
