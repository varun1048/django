from django.shortcuts import render
from .models import Post

def index(req):
    return render(req,"index.html",{"posts":Post.objects.all()})

def post(req,pk):

    return render(req,'posts.html',{"posts":Post.objects.get(id=pk)})