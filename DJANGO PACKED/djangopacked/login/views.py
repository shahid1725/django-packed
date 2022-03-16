from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import forms

class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {"form": form}
        return render(request, "logintemp.html", context)

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("customerview")

            else:
                return render(request, "logintemp.html", {"form": form})