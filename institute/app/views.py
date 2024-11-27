from django.shortcuts import render,redirect
from .models import *
from .models import Contact
from .models import Course
# Create your views here.

def home_view(req):
    nav_links = Course.objects.filter()  
    return render(req, 'home.html', {'nav_links': nav_links})

def about_view(req):
    nav_links = Course.objects.filter()
    return render(req, 'about.html', {'nav_links': nav_links})

def contact_view(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        phone=req.POST['phone']
        subject=req.POST['subject']
        message=req.POST['message']
        data=Contact.objects.create(name=name,email=email,message=message,phone=phone,subject=subject)
        data.save()
        return redirect (contact_view)
    else:
        return render(req,'contact.html')

def courses(req):
    data=Course.objects.all()
    return render(req,'courses.html',{'courses':data})

