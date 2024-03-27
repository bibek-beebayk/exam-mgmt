from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import FileExtensionValidator

from users.models import Stream, Student


class Exam(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    stream = models.ForeignKey(Stream, on_delete=models.PROTECT, related_name="exams")
    is_featured = models.BooleanField(default=False)
    file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=["xlsx", "xls"])])
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


from django.contrib.auth import get_user_model
User = get_user_model()

class ExamAttempt(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.SET_NULL, related_name="exam_attempts")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_attempts")
    obtained_score = models.FloatField(blank=True, null=True)
    exam_data = models.JSONField()
    result_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def calculate_obtained_score(self):
        total = float(0)
        for k, v in self.exam_data.items():
            if v:
                question = Question.objects.get(id=k)
                correct_answer = question.answers.filter(is_correct=True).first()
                if v == correct_answer.id:
                    total += question.weightage
        return total
    
    def get_result_data(self):
        result = []
        for k, v in self.exam_data.items():
            obj = {}
            question = Question.objects.get(id=k)
            obj["question_id"] = k
            obj["question"] = question.description
            obj["question_number"] = question.number
            obj["answer_id"] = v
            if v:
                answer = question.answers.filter(id=v).first().description
            else:
                answer = "N/A"
            obj["answer"] = answer
            correct_answer = question.answers.filter(is_correct=True).first()
            obj["correct_answer_id"] = correct_answer.id
            obj["correct_answer"] = correct_answer.description
            obj["is_correct"] = True if v == correct_answer.id else False
            result.append(obj)
        return result
    
    @property
    def attempted_questions_count(self):
        count = 0
        for k, v in self.exam_data.items():
            if v:
                count += 1
        return count
    
    @property
    def unattempted_questions_count(self):
        count = self.exam.questions.count() - self.attempted_questions_count
        return count

    def save(self, *args, **kwargs):
        if not self.pk:
            self.obtained_score = self.calculate_obtained_score()
            self.result_data = self.get_result_data()
        return super().save(*args, **kwargs)