from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 

from .models import Room,Topic,Message
from .forms import RoomForm

def loginPage(req):
    page = 'login'

    if req.user.is_authenticated:
        return redirect('home')
    if req.method == 'POST':

        username = req.POST.get('username').lower()    
        password = req.POST.get('password')    
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(req,"User does not exits")

        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,"username or password  does not exits")

    return render(req,'base/login_register.html',{
        "page":page,
    })

def logoutUser(req):
    logout(req)
    return redirect('home')

def registerUser(req):

    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username =  user.username.lower()
            user.save()
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,"an error occurred during registration")
        
    return render(req,'base/login_register.html',{
        "form":form
    })

def home(req):
    q =req.GET.get('q') if req.GET.get('q') != None else ''
    rooms  = Room.objects.filter( 
           Q(topic__name__icontains=q) |
           Q(name__icontains=q) |
           Q(description__icontains=q) 
        )
       
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {
        "rooms":rooms,
        'topics':topics,
        'room_count':room_count
        }
    return render(req,'base/home.html',context)

def room(req,pk):
    room =  Room.objects.get(id=pk)
    room_message = room.message_set.all().order_by('-created')
    if req.method == 'POST':
        Message.objects.create(
        user = req.user,
        room = room,
        body = req.POST.get('body')
        )
        return redirect('room',pk=room.id)

    return render(req,'base/room.html',{
        "room":room,"room_message":room_message
        })



@login_required(login_url='login')
def createRoom(req):
    context= {'form':RoomForm()}
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req,'base/room_form.html',context)


@login_required(login_url='login')
def updateRoom(req,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.user != room.host:
        return HttpResponse("your are not allowed here .....")
    else:
        if req.method == 'POST':
            form = RoomForm(req.POST,instance=room)
            if form.is_valid():
                form.save()
                return redirect('home')

    context= {'form': form}
    return render(req,'base/room_form.html',context)


@login_required(login_url='login')
def deleteRoom(req,pk):
    room = Room.objects.get(id=pk)

    if req.user != room.host:
        return HttpResponse("your are not allowed here .....")

    if req.method == 'POST':
        room.delete()
        return redirect('home')
    return render(req,'base/delete.html',{'obj':room})

