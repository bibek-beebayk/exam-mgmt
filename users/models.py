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
    is_student = models.BooleanField(default=True)
