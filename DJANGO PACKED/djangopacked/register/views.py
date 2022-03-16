from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import forms
# Create your views here.


class SignUp(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {}
        context["form"] = form
        return render(request, "user_registration.html", context)

    def post(self,request):
        context={}
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user registered successfully")
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "user_registration.html", context)
