from import_export import resources, fields, widgets
from .models import Exam, Question, Answer


class ExamResource(resources.ModelResource):
    class Meta:
        model = Exam
        fields = ["title"]


class QuestionResource(resources.ModelResource):
    exam = fields.Field(column_name="Exam", attribute="exam", widget=widgets.ForeignKeyWidget(Exam, "title"))
    class Meta:
        model = Question
        fields = ["exam", "number", "description", "weightage"]


class AnswerResource(resources.ModelResource):
    question = fields.Field(column_name="Question", attribute="question", widget=widgets.ForeignKeyWidget(Question, "description"))
    class Meta:
        model = Question
        fields = ["question", "number", "description", "is_correct"]
