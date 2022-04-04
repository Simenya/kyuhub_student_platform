from django.shortcuts import render
from django.http import HttpResponse
# import pyrebase 

# Firbase configuartion
# config{
# apiKey: "AIzaSyA0ASbTI8sJNN7dGEPCR5hpY3pTnPfu3hg",
#   authDomain: "kyuhub-256ug.firebaseapp.com",
#   projectId: "kyuhub-256ug",
#   storageBucket: "kyuhub-256ug.appspot.com",
#   messagingSenderId: "193259981446",
#   appId: "1:193259981446:web:bc6742ea5bc926909b9f07",
#   measurementId: "G-3K90RK8BTZ"
# }

# Create your views here.

def home(request):
    return render(request,"dashboard/index.html")
def resources(request):
    return render(request,"dashboard/resources.html")
def practice(request):
    return render(request,"dashboard/practice.html")
def chat(request):
    return render(request,"dashboard/chat.html")
def statistics(request):
    return render(request,"dashboard/statistics.html")
def settings(request):
    return render(request,"dashboard/settings.html")
def help(request):
    return render(request,"dashboard/help.html")
