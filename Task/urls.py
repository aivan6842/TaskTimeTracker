from django.urls import path, re_path

from . import views
from django.http import StreamingHttpResponse
from .Camera import VideoCamera, gen

urlpatterns = [
    path('signIn/', views.signIn),
    path('signUp/', views.signUp),
    path('viewTasks/<id>/', views.viewTasks),
    path('createTask/<id>/', views.createTask),
    path('cams/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),
    path('', views.home),
]
