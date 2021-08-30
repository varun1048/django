from django.shortcuts import render
# ee6c59eaccc5b0d6b0abb88bc6cee147
# Create your views here.
import json
import urllib.request

def index(res):
    if res.method == "POST":
        city = res.POST['city']
        # openweatherUrl= 'http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=ee6c59eaccc5b0d6b0abb88bc6cee147'
        # json_data = json.loads(urllib.request.urlopen(openweatherUrl).read())
        sssss = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ee6c59eaccc5b0d6b0abb88bc6cee147').read()
        # json_data = json.loads(sssss)

    else:
        city = "" 
    return render(res,'index.html',{'city':city})