from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Room,Topic,Message
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
    page= "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "The user does not exist.")
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password does not exist")

        

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

@login_required(login_url='login')
def delete_message(request,message_id):
    message_obj= Message.objects.get(id=message_id)
    if request.user!=message_obj.user:
        return HttpResponse("You are not allowed here!")
    else:
        message_obj.delete()
        return redirect(request.META.get('HTTP_REFERER'))




def logoutUser(request):
    logout(request)
    return redirect("home")


def registerUser(request):
    form= UserCreationForm()
    page='register'
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"A error occured during registration")
    return render(request,'base/login_register.html',{'form':form})

def home(request):
    q= request.GET.get("q") if request.GET.get("q")!=None else ""
    rooms= Room.objects.filter(Q(topic__name__icontains=q) |
                               Q(name=q) |
                               Q(description__icontains=q)) 
    room_count= rooms.count()
    topics= Topic.objects.all()
    room_messages= Message.objects.filter(Q(room__topic__name__icontains=q))
    return render(request,'base/home.html',{'rooms': rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages})

def room(request, pk):
    room=Room.objects.get(id=pk)
    room.save()
    messages= room.message_set.all().order_by('-created')
    participantss= room.participants.all()
    if request.method=="POST":
        message= Message.objects.create(
            user= request.user,
            room=room,
            body=request.POST.get("body")
        )
        return redirect (request.META.get('HTTP_REFERER'))
    content= {'room':room,'messages': messages,'participants':participantss}
    return render(request, 'base/room.html', content)
@login_required(login_url='/login')
def create_room(request):
    form= RoomForm()
    if request.method=="POST":
        form= RoomForm(request.POST)
        if form.is_valid():
            room= form.save(commit=False)
            room.host= request.user
            room.save()
            return redirect('home')
    context= {'form':form}
    return render(request,'base/room_form.html',context)

def userProfile(request,pk):
    user_obj= User.objects.get(id=pk)
    rooms= user_obj.room_set.all()
    room_messages= user_obj.message_set.all()
    topics= Topic.objects.all()
    context={"user":user_obj,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)


def updateRoom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)
    if request.user !=room.host:
        return HttpResponse("You aren't allowerd user boiiiiii!")
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