from django.shortcuts import render

def home(req):
    return render(req,"box.html")
    
message = []
def add(req):
    message.append(req.POST["message"])
    return render(req,"box.html",{"message":message[::-1]})
    
