from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import orderform
from .models import order
# Create your views here.

def home(request):
    return render(request , 'app1/index.html')

def about(request):
    return render(request , 'app1/about.html')

def book(request):
    ord=orderform()
    if request.method=="POST":
        ord=orderform(request.POST)
        if ord.is_valid():
            ord.save()
            return redirect("orders")
    context={"orders":ord}
    return render(request , 'app1/book.html',context)
def orderdisplay(request):
    products=order.objects.all()
    context={"orders":products}
    return render(request,'app1/display.html',context)


def chef(request):
    return render(request , 'app1/chefs.html')


def event(request):
    return render(request , 'app1/event.html')


def gallery(request):
    return render(request , 'app1/gallery.html')


def menu(request):
    return render(request , 'app1/menu.html' )


def orderdispone(request,pk):
    orders=order.objects.get(id=pk)


    context={"orders":orders}
    return render(request,'app1/menu.html',context)


def update(request,pk):
    orders=order.objects.get(id=pk)
    ord=orderform(instance=orders)
    if request.method=="POST":
        ord=orderform(request.POST,instance=orders)
        if ord.is_valid():
            ord.save()
            return redirect("orders")



    context={"orders":ord}
    return render(request,'app1/book.html',context)