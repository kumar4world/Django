import json
from django.shortcuts import render
from .models import Spanish
import requests

def index(request):
     url = "https://ip-geo-location4.p.rapidapi.com/"
     querystring = {"ip":"76.77.66.98"}
     headers = {
	"X-RapidAPI-Key": "54d89a050bmsh9b85f61a9659597p124bc9jsndf8c172f982b",
	"X-RapidAPI-Host": "ip-geo-location4.p.rapidapi.com"}    
     response = requests.request("GET", url, headers=headers, params=querystring)
     print(response.text)
     data1 = response.json()
     data = Spanish.objects.all()
     print(response.text)
     return render(request, "index.html", {'result': data})    
    
