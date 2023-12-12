from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.profiles,name="profiles"),
    path('profile_user/<pk>/', views.profile_user,name="profile_user"),
    path('login_user', views.login_user,name="login_user"),
    path('register_user', views.registerUser,name="register_user"),
    path('logout_user', views.logout_user,name="logout_user"),
    path('account', views.userAccount,name="userAccount"),
    path('edit_account/<pk>/', views.editAccount,name="editAccount"),
    path('create_skill/', views.create_skill,name="create_skill"),
    path('update_skill/<str:pk>/', views.update_skill,name="update_skill"),
    path('delete_skill/<str:pk>/', views.delete_skill,name="delete_skill"),
]
