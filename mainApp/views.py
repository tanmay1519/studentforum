from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from mainApp.models import user
from mainApp.models import question
from mainApp.models import answer
# Create your views here.
import json
# Create your views here.
from django.http import HttpResponse
def homePage (request):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        branch = request.POST.get('branch')
        User = user(name=name, email=email, password=password, branch=branch)
        User.save()
     return render(request,'mainApp/mainPage.html')
def signin (request):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        branch = request.POST.get('branch')
        User = user(name=name, email=email, password=password, branch=branch)
        User.save()
     return render(request,'mainApp/signin.html')
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        branch = request.POST.get('branch')
        User = user(name=name, email=email, password=password, branch=branch)
        User.save()
    print("Yes")
    #Database instance to be added above this adding success message
    messages.success(request, 'Profile is  Created.')
    return render(request,'mainApp/signup.html')