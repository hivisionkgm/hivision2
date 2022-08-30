from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from.forms import *

# Create your views here.

def home(request):
    if request.method == "POST":
        s = feedbackforms(request.POST)
        if s.is_valid():
            nm = s.cleaned_data['name']
            em = s.cleaned_data['email']
            msg = s.cleaned_data['message']
            x = feedbackmodel(name=nm, email=em, message=msg)
            x.save()
            return render(request, "home.html")
        else:
            return HttpResponse("failed")
    else:
        return render(request,"home.html")

def adminlogin(request):
    if request.method == "POST":
        a = adminforms(request.POST)
        if a.is_valid():
            mail = a.cleaned_data['mail']
            password = a.cleaned_data['password']
            if mail == "mujeebothayoth786@gmail.com" and password == "Hivisionkgm786":
                return redirect('adminhome')
            else:
                return HttpResponse('please enter valid username and password')
    else:
        return render(request,"loginadmin.html")

def adminhome(request):
    a=feedbackmodel.objects.all()
    return render(request,"adminhome.html", { 'data': a })