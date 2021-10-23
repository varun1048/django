import datetime

from django.shortcuts import render,redirect
from .models import Enquirys

from .form import Enquiry_Form
# Create your views here.
def enquirys(req):
    enquirys = Enquirys.objects.all()
    return render(req,'administrator/enquirys.html',{"enquirys":enquirys})

def add_enquiry(req):
    if req.method == 'POST':
        data = req.POST
        # date = data['date']
        # print(date)
        New_enquiry = Enquirys.objects.create(
            name=data['name'],
            number=data['number'],
            message=data['message'],
            joining_date=data['date']
            )
        # New_enquiry.save()
        return redirect("enquirys")

    return render(req,'administrator/add_enquiry.html',{
        "form":Enquiry_Form,
        })

def members(req):
    return render(req,'administrator/members.html')

def add_member(req):
    return render(req,'administrator/add_member.html')

def expiry_members(req):
    return render(req,'administrator/expiry_members.html')






