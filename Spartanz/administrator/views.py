from django.shortcuts import render
from .models import Enquirys,Member
# Create your views here.
def home(req):

    return render(req,'administrator/home.html',{
        "enquirys":len(Enquirys.objects.all()),
        "members":len(Member.objects.all()),
        "attendance":None,
        })

def attendance(req):
    return render(req,'administrator/attendance.html')