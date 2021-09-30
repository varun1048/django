from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

def home(req):
    context = Room.objects.all()
    return render(req,'base/home.html',{"rooms":context})

def room(req,pk):

    context =  Room.objects.get(id=pk)
    return render(req,'base/room.html',{"room":context})

def createRoom(req):
    context= {'form':RoomForm()}
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req,'base/room_form.html',context)

def updateRoom(req,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if req.method == 'POST':
        form = RoomForm(req.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(req,'base/room_form.html',context)


