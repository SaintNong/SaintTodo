from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def inbox(request):
    user = request.user

    # If the user is not logged in, send them to the log in page
    if not user.is_authenticated:
        messages.error(request, "You must be logged in to see your Todo list.")
        return redirect("login")

    # Retrieve the user's tasks, ordered by the task completion status
    tasks = Task.objects.filter(user=user).order_by("completed")
    form = TaskForm()

    return render(
        request,
        "app/inbox.html",
        {
            "tasks": tasks,
            "form": form,
        },
    )

@login_required
def add_task(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.completed = False
            task.save()
        return redirect("inbox")

@login_required
def edit_task(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = Task.objects.filter(id=task_id, user=user).first()
        if task:
            task.title = request.POST.get("title")

        return redirect("inbox")

@login_required
def toggle_task(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = Task.objects.filter(id=task_id, user=user).first()
        if task:
            task.completed = not task.completed
            task.save()
        return redirect("inbox")

@login_required
def delete_task(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        Task.objects.filter(id=task_id, user=user).delete()
        return redirect("inbox")

def settings(request):
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You must be logged in to change your settings.")
        return redirect("login")

    if request.method == "POST":
        # Handle form submission
        theme = request.POST.get('theme', 'light')
        
        # Save the selected theme to the user's profile
        user_profile = request.user.profile
        user_profile.theme = theme
        user_profile.save()

        messages.success(request, "Your settings have been updated.")
        return redirect('settings')

    return render(request, 'app/settings.html')

@login_required
def settings_view(request):
    if request.method == "POST":
        theme = request.POST.get('theme', 'light')
        
        # Save the selected theme to the user's profile
        user_profile = request.user.profile
        user_profile.theme = theme
        user_profile.save()

        messages.success(request, "Settings have been updated.")
        return redirect('settings')

    return render(request, 'app/settings.html')


def statistics(request):
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You must be logged in to see your statistics.")
        return redirect("login")
    
    pending_tasks = Task.objects.filter(user=user, completed=False).count()


    context = {
        'pending_tasks': pending_tasks,
    }

    return render(request, 'app/statistics.html', context)
