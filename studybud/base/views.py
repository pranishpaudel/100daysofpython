from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Room,Topic
from .forms import RoomForm
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

rooms =[
    {'id':1, 'name':'Lets Learn Python!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend Developers'},

]


def login_page(request):

    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')


        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, "User not found error.")
    context= {}
    return render(request,'base/login_register.html',context)
def home(request):
    q= request.GET.get("q") if request.GET.get("q")!=None else ""
    rooms= Room.objects.filter(Q(topic__name__icontains=q) |
                               Q(name=q) |
                               Q(description__icontains=q)) 
    room_count= rooms.count()
    topics= Topic.objects.all()
    return render(request,'base/home.html',{'rooms': rooms,'topics':topics,'room_count':room_count})

def room(request, pk):
    room=Room.objects.get(id=pk)
    content= {'room':room}
    return render(request, 'base/room.html', content)


def create_room(request):
    form= RoomForm()
    if request.method=="POST":
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form':form}
    return render(request,'base/room_form.html',context)



def updateRoom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)
    if request.method=="POST":
        form= RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form':form}
    return render(request,'base/room_form.html',context)


def deleteRoom(request,pk):
    room= Room.objects.get(id=pk)
    if request.method=="POST":
        room.delete()
        redirect ('home')
    return render(request,'base/delete.html',{'obj': room})