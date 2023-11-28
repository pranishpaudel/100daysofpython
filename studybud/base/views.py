from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# Create your views here.
from django.http import HttpResponse

rooms =[
    {'id':1, 'name':'Lets Learn Python!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend Developers'},

]
def home(request):
    rooms= Room.objects.all
    return render(request,'base/home.html',{'rooms': rooms})

def room(request, pk):
    room=Room.objects.get(id=pk)
    content= {'room':room}
    return render(request, 'base/room.html', content)


def create_room(request):
    form= RoomForm()
    context= {'form':form}
    return render(request,'base/room_form.html',context)