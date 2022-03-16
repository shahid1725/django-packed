from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from . import forms
from django.contrib.auth.models import User


# Here the code below of an employee creation and its
# associated crud function like list,update,delete

# CREATION OF EMPLOYEE
#----------------------

#class_based_view

class CreateEmply(CreateView):
    model = User
    success_url =reverse_lazy("listemployee")
    form_class = forms.EmployeeCreationForm
    template_name = "employee_create.html"

#function_based_view

class CreateEmployee(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.EmployeeCreationForm()
        context = {}
        context["form"] = form
        return render(request, "employee_create.html", context)

    def post(self,request):
        context={}
        form = forms.EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Employee Created successfully")
            return redirect("email")
        else:
            context["form"] = form
            return render(request, "employee_create.html", context)

# LISTING THE CREATED EMPLOYEES
#-------------------------------

class ListEmployee(ListView):
    model = User
    template_name = "employee_list.html"
    context_object_name = "employees"

# UPDATE / EDIT  CREATED EMPLOYEE
#----------------------------------

class UpdateEmployeeView(UpdateView):
    model = User
    form_class = forms.EmployeeCreationForm
    success_url = reverse_lazy("listemployee")
    pk_url_kwarg = "id"
    template_name = "employee_edit.html"

# DELETE THE CREATED EMPLOYEE
#-------------------------------

class DeleteEmployeeView(DeleteView):
    model = User
    template_name = "employee_delete.html"
    success_url = reverse_lazy("listemployee")
    pk_url_kwarg = "id"