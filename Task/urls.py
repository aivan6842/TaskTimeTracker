from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.signIn),
    path('signUp/', views.signUp),
    path('viewTasks/<id>/', views.viewTasks),
    path('createTask/<id>/', views.createTask),
]
