from os import name
from django.shortcuts import render
from .models import Music
# Create your views here.
def login(req):
    obj = Music.objects.all()
    return render(req,'login.html',{"obj":obj})

def main(req):
    # req.Post
    info ={
        "song":req.POST['song'],
        "artist":req.POST['artist']
    }
    print(req.POST['song'])
    return render(req,'main.html',info)