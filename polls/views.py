# added new changes in views
from django.shortcuts import render

def Home(request):
    return render(request,'Home.html',{})

def about(request):
    return render(request,'about.html',{})