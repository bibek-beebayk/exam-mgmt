from django.contrib import admin
from .models import Exam, ExamAttempt, Question, Answer
from import_export.admin import ImportMixin
from .resource import ExamResource, QuestionResource, AnswerResource
import pandas as pd


# admin.site.name = "Admin"
# admin.site.site_title = "Admin"
# admin.site.site_header = "Admin"


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    # actions = ["import_from_excel"]
    list_display = ["title", "stream", "is_free", "is_practice_test"]
    list_filter = ["stream", "is_free", "is_practice_test"]

    def save_model(self, request, obj, form, change):
        if obj.pk:
            return super().save_model(request, obj, form, change)
        super().save_model(request, obj, form, change)

        # Handle Excel file upload
        if obj.file:
            file_path = obj.file.path
            df = pd.read_excel(file_path)

            # Iterate through rows and create Question and Answer objects
            for index, row in df.iterrows():
                question = Question.objects.create(
                    exam=obj,
                    number=index + 1,
                    description=row['Question'],
                    weightage=row['Weightage']
                )

                # Create Answer objects
                for i in range(1, 5):
                    answer_text = row[f'Answer {i}']
                    is_correct = row['Correct Answer'] == i
                    Answer.objects.create(
                        question=question,
                        number=i,
                        description=answer_text,
                        is_correct=is_correct
                    )
            if not obj.title or obj.title == "":
                obj.title = obj.file.name.split(".")[0].strip()
                obj.save()
        else:
            self.message_user(request, "No file uploaded.")


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ["exam", "student", "timestamp"]