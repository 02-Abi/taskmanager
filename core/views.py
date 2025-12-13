from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("dashboard")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "dashboard.html", {"tasks": tasks})


@login_required
def create_task_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        remind_at = request.POST.get("remind_at")

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            remind_at=remind_at,
        )

        return redirect("dashboard")

    return render(request, "create_task.html")


@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect("dashboard")
