from django.urls import path
from . import views


urlpatterns = [
    path('project/<pk>/', views.project,name="project"),
    path('create_project/', views.create_project,name="create_project"),
    path('', views.projects,name="home"),
]
