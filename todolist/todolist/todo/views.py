from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout 
from .forms import RegisterForm, TaskForm 
from django.contrib import messages 
from .models import Task 

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def main(request):
    tasks = Task.objects.all()
    return render(request, 'base/main.html', {'tasks': tasks})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome, {}".format(user.username))
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below!")
    
    else:
        form = RegisterForm()

    return render(request, 'base/register.html', {'form': form})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else: 
        form = TaskForm()
    
    return render(request, 'base/task_create.html', {'form': form})


def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'base/task_details.html', {'task': task})

def reset(request):
    return render(request, 'reset.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username, password1=password1)
        if user is not None: 
            login(request, user)
            messages.success(request, "User logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, 'Username or password is invalid!')
    
    return render(request, 'base/login.html')
   
def logout_view(request):
    logout(request)
    return redirect('login')

def delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('main')
    return render(request, 'base/task_delete.html', {'task': task})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('main')
    else: 
        form = TaskForm(instance=task)
    
    return render(request, 'base/task_edit.html', {'form': form, 'task': task})



    
