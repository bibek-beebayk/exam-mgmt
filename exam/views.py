from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


from exam.models import Exam, ExamAttempt
from users.models import Student


def index_view(request):
    context = {}
    user = request.user
    try:
        stream = request.user.student.stream
    except:
        stream = None
    if not stream:
        exams = Exam.objects.exclude(is_practice_test=True)[:3]
    else:
        exams = Exam.objects.filter(stream=stream).exclude(is_practice_test=True)[:3]
    context["exams"] = exams
    return render(request, "index.html", context)


def practice_test_view(request):
    context = {}
    user = request.user
    try:
        stream = request.user.student.stream
    except:
        stream = None
    if not stream:
        exams = Exam.objects.filter(is_practice_test=True)[:3]
    else:
        exams = Exam.objects.filter(stream=stream, is_practice_test=True)[:3]
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
        time_taken = data.pop("elapsed_time")
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
            exam_data = filtered_data,
            time_taken=time_taken[0]
        )
        context = {"result": exam_attempt.result_data, "exam": exam, "attempt": exam_attempt}
        return render(request, "exam_summary.html", context)
    

def exam_summary_view(request, pk):
    exam_attempt = ExamAttempt.objects.get(id=pk)
    exam = exam_attempt.exam
    context = {"result": exam_attempt.result_data, "exam": exam, "attempt": exam_attempt}
    return render(request, "exam_summary.html", context)
    