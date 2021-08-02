from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("review",views.review,name="review"),

    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("register",views.register,name="register")
]