from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


from exam.models import Exam, ExamAttempt


def index_view(request):
    context = {}
    exams = Exam.objects.all()[:3]
    context["exams"] = exams
    return render(request, "index.html", context)


from copy import deepcopy
class ExamDetailView(DetailView):
    model = Exam

    def post(self, request, *args, **kwargs):
        exam = self.get_object()
        data = deepcopy(request.POST)
        data.pop("csrfmiddlewaretoken")
        # import ipdb; ipdb.set_trace()
        if not request.user.id:
            student_id = None
        else:
            student_id = request.user.id
        exam_attempt = ExamAttempt.objects.create(
            # student_id=student_id,
            exam=exam,
            exam_data = data
        )
        return HttpResponse("Success")