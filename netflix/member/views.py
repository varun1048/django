from django.shortcuts import render ,redirect

# Create your views here.
from django.contrib.auth.models import User,auth
from django.contrib import messages


def index(req):
    return render(req,'index.html')


def login(req):
    if req.method == 'POST':
        user = auth.authenticate(
            username=req.POST['username'],
            password=req.POST['password']
        )
        if user is not None:
            auth.login(req,user)
            return  redirect('index')
        else:
            messages.info(req,"Check your information")

    return render(req,'login.html')

def register(req):
    info = req.POST
    if req.method == 'POST':
        if User.objects.filter(username=info["username"]).exists():
            messages.info(req,"user name tacken")
            return redirect('register')
        elif info['password'] != info['password1']:
            messages.info(req,"password not  match")
            return redirect('register')
        else:
            User.objects.create_user(username=info['username'],password=info['password'])
            return redirect('login')
    
    return render(req,'register.html')

def logout(req):
    auth.logout(req)
    return redirect('/')