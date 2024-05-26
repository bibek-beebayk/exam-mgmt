from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                student = user.student
            except:
                student = None
            # import ipdb; ipdb.set_trace()
            if not student:
                messages.error(request, "You need to have a student account to login.")
                # raise ValueError("You need to have a student account to login.")
                return redirect("login")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    student = request.user.student
    context = {}
    recent_exams = student.exam_attempts.order_by("-timestamp")
    page_number = request.GET.get("page")
    paginator = Paginator(recent_exams, 20)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        
    # context["recent_exams"] = page_obj.object_list
    # context["paginator"] = page_obj.paginator
    context["page_obj"] = page_obj
    # import ipdb; ipdb.set_trace()

    return render(request, "user_profile.html", context)