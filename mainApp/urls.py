from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.homePage,name="homePage"),
    path("signin/",views.signin,name="signinPage"),
    path("signup/",views.signup,name="signupPage")
]