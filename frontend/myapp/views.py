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
    # info = reviewModels.objects.all()
    # return render(req,'review.html',{"reviews":info})

    

        

def register(req):
    return render(req,'register.html')