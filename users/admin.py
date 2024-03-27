from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Stream, Student, Teacher, User, Interest
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Q


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # change_user_password_template = None
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
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "password1", "password2"),
    #         },
    #     ),
    # )

    readonly_fields = ["is_superuser", "is_staff", "groups", "user_permissions"]
    list_display = ["username", "full_name", "date_joined"]

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.is_superuser = True
        obj.is_staff = True
        return super().save_model(request, obj, form, change)

    def full_name(self, obj):
        return obj.__str__()

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        student_ids = Student.objects.values_list("id", flat=True)
        teacher_ids = Teacher.objects.values_list("id", flat=True)
        return super().get_queryset(request).exclude(Q(id__in=student_ids) | Q(id__in=teacher_ids))
    

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(UserAdmin):
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
                "date_joined",
                "stream"
            ]
        }),
        ("Permissions", {
            "fields": [
                "groups",
                "user_permissions"
            ]
        })
    ]
    list_display = list_display = ["username", "full_name", "date_joined", "stream"]
    
    def get_queryset(self, request):
        return Student.objects.all()
    
    def save_model(self, request, obj, form, change):
        obj.is_staff = False
        obj.is_superuser = False
        return obj.save()


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    
    readonly_fields = ["is_superuser", "is_staff", "user_permissions"]

    def get_queryset(self, request):
        return Teacher.objects.all()
    
    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        obj.is_superuser = False
        return obj.save()