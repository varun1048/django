from django.urls import path
from . import views
from . import views2
urlpatterns = [
    path('',views.home,name='main'),
    path('attendance',views.attendance,name='attendance'),

    path('enquirys',views2.enquirys,name='enquirys'),
    path('add_enquiry',views2.add_enquiry,name='add_enquiry'),
    path('members',views2.members,name='members'),
    path('add_member',views2.add_member,name='add_member'),
    path('expiry_members',views2.expiry_members,name='expiry_members'),
]
