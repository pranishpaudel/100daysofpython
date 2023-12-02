from django.urls import path
from . import views


urlpatterns = [
    path('project/<pk>/', views.project,name="project"),
    path('', views.projects,name="home"),
]
