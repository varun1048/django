from django.shortcuts import render

# Create your views here.
def enquirys(req):
    return render(req,'administrator/enquirys.html')

def add_enquiry(req):
    return render(req,'administrator/add_enquiry.html')

def members(req):
    return render(req,'administrator/members.html')

def add_member(req):
    return render(req,'administrator/add_member.html')

def expiry_members(req):
    return render(req,'administrator/expiry_members.html')






