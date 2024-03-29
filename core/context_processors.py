from django.contrib.auth import get_user_model
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

from users.models import Student
from exam.models import Exam, ExamAttempt

User = get_user_model()


def get_graph_data(request):
    import plotly.offline as pyo
    import plotly.graph_objs as go
    import pandas as pd
    import plotly.express as px
    import datetime as dt
    import calendar

    data = Purchase.objects.values("purchased_date__month", "purchased_date__year").annotate(total=Sum("amount")).order_by("purchased_date__year", "purchased_date__month")
    data_list = [x for x in data]
    slice_index = len(data_list) - 12
    sliced_list = data_list[slice_index : None]
    months_map = {
        1: "January",
        2: "February", 
        3: "March",
        4: "April", 
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    data_list = []
    for obj in sliced_list:
        item = {
            "month": f"{months_map[obj['purchased_date__month']]} {obj['purchased_date__year']}",
            "amount": obj["total"]
        }
        data_list.append(item)

    if not data_list:
        item = {
            "month": "No data",
            "amount": "No data"
        }
        data_list.append(item)

    df = pd.DataFrame(data_list)

    fig = px.line(df, x='month', y='amount', title='Earnings Over Months', line_shape="spline", markers=True)
    

    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 20, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })

    plt_div = pyo.plot(fig, output_type="div")
    return plt_div


from django.utils import timezone

def context_users_info(request):
    extra_context = {}
    if request.path == "/admin/":

        students_count = Student.objects.count()
        extra_context["users_count"] = students_count

        month_new_students = Student.objects.filter(date_joined__month=timezone.now().month).count()
        extra_context["month_new_students"] = month_new_students

        total_exams_count = Exam.objects.count()
        extra_context["exams_count"] = total_exams_count

        total_exam_attempts = ExamAttempt.objects.count()
        extra_context["exam_attempts"] = total_exam_attempts

        # extra_context["plt_div"] = get_graph_data(request)
    return extra_context
