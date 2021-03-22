from django.shortcuts import render

# Create your views here.
import json
# Create your views here.
from django.http import HttpResponse
def homePage (request):
    return render(request,'mainApp/mainPage.html')
def signin (request):
    return render(request,'mainApp/signin.html')
def signup(request):
    print("Yes")
    return render(request,'mainApp/signup.html')