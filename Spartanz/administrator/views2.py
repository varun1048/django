import datetime

from django.shortcuts import render,redirect
from .models import Enquirys,Member

from .form import Enquiry_Form
# Create your views here.
def enquirys(req):
    enquirys = Enquirys.objects.all()
    return render(req,'administrator/enquirys.html',{"enquirys":enquirys})

def add_enquiry(req):
    if req.method == 'POST':
        data = req.POST
        number = int(data['number'])
        New_enquiry = Enquirys.objects.create(
            name=data['name'],
            number= number,
            message=data['message'],
            joining_date=data['date'],
            visit_type= data['visit_type']
            )
        New_enquiry.save()
        return redirect("enquirys")

    return render(req,'administrator/add_enquiry.html')















def members(req):
    
    return render(req,'administrator/members.html',{"members":Member.objects.all()})

def member(req,member_id):
    member =  Member.objects.get(id=member_id)
    return render(req,'administrator/member.html',{"member":member})




def add_member(req):
    return render(req,'administrator/add_member.html')

def expiry_members(req):
    return render(req,'administrator/expiry_members.html')






