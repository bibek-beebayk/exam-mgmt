from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect("home")
        else:
            # Return an 'invalid login' error message
            messages.error(request, "Invalid username or password.")
    # If GET request or invalid form submission, render the login page with an empty form
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")