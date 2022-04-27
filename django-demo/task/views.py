from django.shortcuts import render

# Create your views here.


def index(request) :
    return render(request, "tasking/index.html")

def page(request) :
    return render(request,"tasking/pokeball.html")

def lorem(request) :
    return render(request, "tasking/lorem.html")

def back(request) :
    return render(request, "tasking/index.html")




