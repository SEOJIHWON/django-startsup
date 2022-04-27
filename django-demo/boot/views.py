

from django.shortcuts import render, redirect
from django.contrib.auth.models  import User
from django.contrib import auth
from boot.models import Inquiry
# from blog.models import Blog
# Create your views here.


def test(request) :
    
    return render (request, "base.html" , )


def blog(request) :
     if not request.user.ist_authenticated :
        return redirect ("boot:login")
     return render (request, "boot/blog.html" )
    

def home(request) : 
    print(request.user.is_authenticated)
    
    return render (request, "boot/index.html", ) 

def contact(request) :

    if request.method == "GET" :
        return render (request, "boot/contact.html")

    elif request.method == "POST":

        new_inquiry = Inquiry()
        new_inquiry.fullname = request.POST["fullname"]
        new_inquiry.emailaddress = request.POST["emailaddress"]
        new_inquiry.phonenum = request.POST["phonenum"]
        new_inquiry.message = request.POST["message"]
        new_inquiry.save()

    # return HttpResponseRedirect (reverse("landing:read-all"))
    return redirect("boot:contact")



   
    
    

def about(request) :  
    
    return render (request, "boot/about.html",) 


def sign_up(request) :
    

 
        
     
    if request.method == "POST" :

            new_user=User()
            new_user.username = request.POST.get("username")
            new_user.password = request.POST.get("password")
            new_user.password_check = request.POST.get("password_check")

            if new_user.username is not None and new_user.password is not None and \
                new_user.password == new_user.password_check :

                 new_user = User.objects.create_user(
                    username = new_user.username,
                    password = new_user.password )
            
            return redirect("boot:home")

    return render (request, "boot/sign-up.html")
    #  if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     password_check = request.POST.get("password_check")
    #     if username is not None and \
    #         password is not None and \
    #         password == password_check:
            
    #         new_user = User.objects.create_user(
    #             username=username,
    #             password=password,
    #         )
            
    #         return redirect("boot:home")

    # return render(request, "boot/sign-up.html")
        
    

   






def login(request) :
    if request.user.is_authenticated :
        return redirect ("boot:home")
    context ={

    }


    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
         
        user = auth.authenticate(
            request,
            username = username,
            password = password 
        )

        if user is not None :
            auth.login(request ,user)
            return redirect ("boot:home")


    return render (request, "boot/login.html",  context=context)


def logout (request) :
    print(request.user.is_authenticated)
    if request.method == "POST" :
        auth.logout(request)

    return redirect("boot:home")



