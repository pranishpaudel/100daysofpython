from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.profiles,name="profiles"),
    path('profile_user/<pk>/', views.profile_user,name="profile_user"),
]
