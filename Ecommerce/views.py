
from django.contrib import messages
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string

def index(request):
    return render(request, "welcome.html");

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        firstname= request.POST["firstname"]
        lastname= request.POST["lastname"]
        gmail= request.POST["gmail"]
        password1= request.POST["password1"]
        password2= request.POST["password2"]

        user= User.objects.create_user(username= username, password=password1,email=gmail)
        user.first_name=firstname
        user.last_name=lastname
        user.save()


        ## registatiton successful mail to user.

        # subject= "Welcome to the Apna Mart,  Indias Biggest online Shopping platform "
        # body= "Thank You"
        # mail_from= settings.EMAIL_HOST_USER
        # recipent_mail=[user.email,]
        # send_mail(subject, body, mail_from, recipent_mail )

        # ---------------------------or better way <> below mentiond-------------------------------------

        template= render_to_string("email_template.html",{"name":user.first_name})

        email_message=EmailMessage("Welcome to Apna Mart",
                             template, 
                            settings.EMAIL_HOST_USER,
                            [user.email]
                            )
        email_message.send()

        return redirect("ShopName")
    return render(request, "signup.html")

def userlogin(request):
    if request.method=='POST':
        loginusername= request.POST["loginusername"]
        loginpassword= request.POST["loginpassword"]
       
        user= authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You have Successfully logged in")
            # return redirect("ShopName")
            return redirect("/")
        else:
            messages.errors(request, "Invalid Login or Don't have an account please sign up")
            return render(request, "login.html")
    return render(request, "login.html")


def userlogout(request):
    logout(request)
    messages.success(request, "You have successfully logout")
    return redirect("/")

