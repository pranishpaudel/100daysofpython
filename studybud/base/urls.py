from django.urls import path
from . import views


urlpatterns= [
    path('login/',views.login_page,name="login_page"),
    path('delete_message/<message_id>',views.delete_message,name="delete_message"),
    path('register/',views.registerUser,name="registerUser"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create_room/',views.create_room,name="create_room"),
    path('update_room/<str:pk>',views.updateRoom,name="update_room"),
    path('delete_room/<str:pk>',views.deleteRoom,name="delete_room"),
]
