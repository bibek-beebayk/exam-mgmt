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
    return render(request, "user_profile.html", {})