from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.



def signout(request):
    logout(request)
    return redirect("signin")
