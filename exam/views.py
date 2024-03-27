from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


from exam.models import Exam, ExamAttempt
from users.models import Student


def index_view(request):
    context = {}
    exams = Exam.objects.all()[:3]
    context["exams"] = exams
    return render(request, "index.html", context)


def homepage(request):
    return render(request, "homepage.html", {})


from copy import deepcopy
class ExamDetailView(DetailView):
    model = Exam

    def post(self, request, *args, **kwargs):
        exam = self.get_object()
        data = deepcopy(request.POST)
        data.pop("csrfmiddlewaretoken")
        filtered_data = {}
        for obj in exam.questions.all():
            filtered_data[obj.id] = None
        for k, v in data.items():
            filtered_data[int(k)] = int(v)
        try:
            if request.user.student:
                student_id = request.user.id
            else:
                student_id = request.user.id
        except:
            student_id = None
        exam_attempt = ExamAttempt.objects.create(
            student_id=student_id,
            exam=exam,
            exam_data = filtered_data
        )
        context = {"result": exam_attempt.result_data, "exam": exam, "attempt": exam_attempt}
        return render(request, "exam_summary.html", context)