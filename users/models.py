from django.db import models
from django.contrib.auth.models import AbstractUser


class Interest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name or ""} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name


class Stream(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self) -> str:
        return self.short_name if self.short_name else self.name


class Student(User):
    stream = models.ForeignKey(Stream, related_name="students", on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(User):
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
