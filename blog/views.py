from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html') 

def team(request):
    return render(request,'team.html') 

def contact(request):
    return render(request,'contact.html') 

def category(request):
    return render(request,'category.html') 