from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name="questions", on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
    weightage = models.FloatField(default=1.0)

    def __str__(self) -> str:
        return f"{self.exam.title}: {self.number}"
    

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
    is_correct = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.question.__str__()}: {self.description}"
