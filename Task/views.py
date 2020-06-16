from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import UserForm, TaskForm
from .models import User, Task
import datetime

# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'homePage.html')
    elif request.POST.get('signInButton'):
        return redirect('/signIn/')
    elif request.POST.get('signUpButton'):
        return redirect('/signUp/')
    return render(request, 'homePage.html')

def signIn(request):
    if request.method == 'POST':
        if request.POST.get('signUp'):
            return redirect('/signUp/')
        username = request.POST['username']
        password = request.POST['password']
        userExists = User.objects.filter(username=username, password=password).exists()
        if userExists:
            user = User.objects.get(username=username, password=password)
            return redirect(f'/viewTasks/{user.id}/')
        return render(request, 'signIn.html', {'BadUser': True})
    else:
        return render(request, 'signIn.html', {'BadUser': False})


def signUp(request):
    if request.method == 'POST':
        if request.POST.get('signIn'):
            return redirect('/signIn/')
        username = request.POST['username']
        usernameExists = User.objects.filter(username=username).exists()
        if not usernameExists:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                currUser = User.objects.get(username=request.POST['username'], password=request.POST['password'])
                return redirect(f'/viewTasks/{currUser.id}/')
        return render(request, 'signUp.html', {'BadUser':True})
    else:
        return render(request, 'signUp.html', {'BadUser': False})

def viewTasks(request, id):
    allTasks = Task.objects.filter(userReference__id=id)
    if request.method == 'GET':
        return render(request, 'viewTasks.html', {'userTasks': allTasks })
    else:
        if request.POST.get('createTask'):
            return redirect(f'/createTask/{id}/')
        else:
            for task in allTasks:
                if request.POST.get(f'{task.taskName}Start'):
                    currTask = Task.objects.get(id=task.id)
                    currTask.currentlyWorking = True
                    #currTask.startedAt = datetime.datetime.now()
                    currTask.save()
                    break
                elif request.POST.get(f'{task.taskName}Stop'):
                    currTask = Task.objects.get(id=task.id)
                    currTask.currentlyWorking = False
                    #currTask.totaltime = datetime.datetime.now() - currTask.startedAt
                    currTask.save()
                    break
                elif request.POST.get(f'{task.taskName}Delete'):
                    currTask = Task.objects.get(id=task.id)
                    currTask.delete()
            allTasks = Task.objects.filter(userReference__id=id)
            return render(request, 'viewTasks.html', {'userTasks': allTasks})

def createTask(request, id):
    if request.method == 'GET':
        return render(request, 'createTask.html', {'BadTaskName': False})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            currForm = form.save(commit=False)
            taskNameExists = Task.objects.filter(taskName=currForm.taskName).exists()
            if taskNameExists:
                return render(request, 'createTask.html', {'BadTaskName': True})
            userRef = User.objects.get(id=id)
            currForm.userReference = userRef
            currForm.save()
            return redirect(f'/viewTasks/{id}/')
        else:
            return HttpResponse('Invalid Form')
        return render(request, 'createTask.html')
