from django.urls import path, re_path

from . import views

urlpatterns = [
    path('signIn/', views.signIn),
    path('signUp/', views.signUp),
    path('viewTasks/<id>/', views.viewTasks),
    path('createTask/<id>/', views.createTask),
    path('train/<id>/', views.getTrainingData),
    path('match/', views.match),
    path('', views.home),
]
