from os import name
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import reviewModels #database bro
# Create your views here.
def index(req):            
    return render(req,'index.html',{"review":reviewModels})

def review(req):
    # info = {"review":req.POST['review']}
    # info = User.objects.all() #also can do this way
    # return render(req,'review.html ',info)    
    info = reviewModels.objects.all()
    return render(req,'review.html',{"reviews":info})
  

def register(req):
    if req.method == 'POST':
        password1 = req.POST['password1']
        password2 =  req.POST['password2']
        name =  req.POST['name']

        if password2 != password1:
            print(password1 +"-----"+name)
            messages.info(req,"password not match")
            return redirect('register')
        elif User.objects.filter(username=name).exists():
            messages.info(req,"name is exists bro")
            return redirect('register')
        else:
            password =password1
            user = User.objects.create_user(username=name,password=password)
            user.save()
            return redirect('login')
    else:
        return render(req,'register.html')

def logout(req):
    auth.logout(req)
    return redirect('/')


def login(req):
    if req.method == 'POST':
        username=req.POST['name']
        password=req.POST['password']

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(req,user)
            return redirect('/')

        else:
            messages.info(req,"go out you B*** ")
            return redirect('login')
    else:
        return render(req,'login.html')