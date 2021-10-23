from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'administrator/home.html')

def attendance(req):
    return render(req,'administrator/attendance.html')