from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


from exam.models import Exam, ExamAttempt, LiveExam
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
    context["free_exams"] = Exam.objects.filter(is_free=True)
    context["exams"] = exams
    context["live_exams"] = LiveExam.objects.order_by("-id")
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
    context["free_exams"] = Exam.objects.filter(is_free=True)
    return render(request, "index.html", context)


def homepage(request):
    context = {}
    free_exams = Exam.objects.filter(is_free=True)[:3]
    context["free_exams"] = free_exams
    return render(request, "homepage.html", context)


from copy import deepcopy
from django.contrib import messages


class ExamDetailView(DetailView):
    model = Exam

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated and not self.get_object().is_free:
            messages.error(request, "You need to login first.")
            return redirect("login")
        return super().get(request, *args, **kwargs)

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
            exam_data=filtered_data,
            time_taken=time_taken[0],
        )
        context = {
            "result": exam_attempt.result_data,
            "exam": exam,
            "attempt": exam_attempt,
        }
        return render(request, "exam_summary.html", context)


def exam_summary_view(request, pk):
    exam_attempt = ExamAttempt.objects.get(id=pk)
    exam = exam_attempt.exam
    context = {
        "result": exam_attempt.result_data,
        "exam": exam,
        "attempt": exam_attempt,
    }
    return render(request, "exam_summary.html", context)


def live_exam_view(request, pk):
    live_exam = LiveExam.objects.get(id=pk)

    if request.method == "POST":
        exam = live_exam.exam
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
            exam_data=filtered_data,
            time_taken=time_taken[0],
            live_exam=True
        )
        context = {
            "result": exam_attempt.result_data,
            "exam": exam,
            "attempt": exam_attempt,
        }
        return render(request, "exam_summary.html", context)

    if live_exam.status.lower() == "not started":
        messages.error(request, "The test has not begun yet.")
        return redirect("index")
    if live_exam.status.lower() == "ended":
        messages.error(request, "The test has already ended.")
        return redirect("index")
    context = {}
    context["object"] = live_exam
    return render(request, "live_exam.html", context)
