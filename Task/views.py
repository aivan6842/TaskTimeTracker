from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import UserForm, TaskForm, ImageForm
from .models import User, Task, TrainImage
from django.utils import timezone
from .Camera import VideoCamera, face_capture
import cv2
import face_recognition

# Create your views here.
def getTrainingData(request, id):
    if request.method == 'POST':
        if request.POST.get('noID'):
            return redirect(f'/viewTasks/{id}/')
        userRef = User.objects.get(id=id)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            for item in request.FILES.getlist('image'):
                TrainImage.objects.create(userReference=userRef, image=item)
            return redirect(f'/viewTasks/{id}/')

    return render(request, 'uploadImages.html')

def match(request):
    cam = VideoCamera()
    all = TrainImage.objects.all()
    TOLERANCE = 0.6
    MODEL = "hog"

    known_faces = []
    known_names = []

    print('loading known faces')

    for pic in all:
        image = face_recognition.load_image_file(pic.image)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(pic.userReference)

    while True:
        ret, image = cam.video.read()

        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                return redirect(f'/viewTasks/{match.id}/')

def home(request):
    return redirect('/signIn/')

def signIn(request):
    if request.method == 'POST':
        if request.POST.get('signUp'):
            return redirect('/signUp/')
        elif request.POST.get('signInFaceID'):
            return redirect('/match/')

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
                return redirect(f'/train/{currUser.id}/')

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
        elif request.POST.get('signOut'):
            return redirect(f'/signIn/')
        else:
            for task in allTasks:
                if request.POST.get(f'{task.taskName}Start'):
                    currTask = Task.objects.get(id=task.id)
                    currTask.currentlyWorking = True
                    currTask.startedAt = timezone.now()
                    currTask.save()
                    break
                elif request.POST.get(f'{task.taskName}Stop'):
                    currTask = Task.objects.get(id=task.id)
                    currTask.currentlyWorking = False
                    currTask.totaltime += timezone.now() - currTask.startedAt
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
