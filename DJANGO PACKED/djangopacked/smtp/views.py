from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


# We have added smtp emial setup in settings.py

def sendanemail(request):
  if request.method == "POST":
      to = request.POST.get('toemail')
      content = request.POST.get('content')
      print(to,content)
      send_mail(
          #subject
          "testing",
          #msg
          content,
          #from email
          settings.EMAIL_HOST_USER,
          #rec list
          [to]
      )
      return redirect('listemployee')
  else:
      return render(
          request,
          'employee_email.html',
          {
              'title':'send an email'
          }
      )