from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based view , class based view

def home(request):
    return HttpResponse("HOME")

def index(request):
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request,'aboutus.html')

def contactUs(request):
    name = "Ram"
    email = "ram@gmail.com"
    contact = {'name':name,'email':email}
    return render(request,'blog/contactus.html',contact)

def feedback(request):
    userName = "parth"
    userEmail = "parth@gmail.com"
    context ={
        'userName':userName,
        'userEmail':userEmail,
    } 
    return render(request,'blog/feedback.html',context)

def stickysocialbar(request):
    return render(request,'blog/stickysocialbar.html')

def coupon(request):
    return render(request,'blog/coupon.html')

def video(request):
    return render(request,'blog/video.html')