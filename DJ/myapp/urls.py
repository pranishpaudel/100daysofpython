from django.urls import path
from . import views


urlpatterns = [
    path('project/<pk>/', views.project,name="project"),
    path('create_project/', views.create_project,name="create_project"),
    path('update_project/<pk>', views.update_project,name="update_project"),
    path('delete_project/<pk>', views.delete_project,name="delete_project"),
    path('', views.projects,name="home"),
]
