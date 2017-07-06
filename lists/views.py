from django.shortcuts import render
from django.http import HttpResponse

def home_page(HttpRequest):
#    return HttpResponse('<html><title>To-Do Lists</title></html>')
    return render(HttpRequest, 'home.html')

# Create your views here.
