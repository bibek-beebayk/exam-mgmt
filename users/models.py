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
    email = models.EmailField(blank=True, null=True)

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
    has_subscription = models.BooleanField(default=False)

    @property
    def total_tests_taken(self):
        return self.exam_attempts.count() or 0
    
    @property
    def highest_score(self):
        return self.exam_attempts.order_by("-obtained_score").first().obtained_score or 0
    

    @property
    def highest_scoring_exam(self):
        return self.exam_attempts.order_by("-obtained_score").first().exam.title or "N/A"
    
    @property
    def lowest_score(self):
        return self.exam_attempts.order_by("obtained_score").first().obtained_score or 0
    

    @property
    def lowest_scoring_exam(self):
        return self.exam_attempts.order_by("obtained_score").first().exam.title or "N/A"
    

    @property
    def average_score(self):
        average_score = self.exam_attempts.aggregate(average=models.Avg(models.F("obtained_score")))["average"] or 0
        return round(average_score, 2)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(User):
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
