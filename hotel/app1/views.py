from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request , 'app1/index.html')

def about(request):
    return render(request , 'app1/about.html')

def book(request):
    return render(request , 'app1/book.html')



def chef(request):
    return render(request , 'app1/chefs.html')


def event(request):
    return render(request , 'app1/event.html')


def gallery(request):
    return render(request , 'app1/gallery.html')


def menu(request):
    return render(request , 'app1/menu.html' )