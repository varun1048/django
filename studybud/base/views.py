from django.shortcuts import render
from .models import Room

def home(req):
    context = Room.objects.all()
    return render(req,'base/home.html',{"rooms":context})

def room(req,pk):

    context =  Room.objects.get(id=pk)
    return render(req,'base/room.html',{"room":context})


