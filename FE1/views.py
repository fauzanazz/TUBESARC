from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import * 

def signuppage(request):
    # return HttpResponse("Hello world!")
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Please enter your password corectly!")
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')

    return render (request, template_name='signuppage.html')


def loginpage(request):
    # return HttpResponse("Hello world!")
    if request.method=='POST':
        username = request.POST.get("user")
        password = request.POST.get("pass")

        user = authenticate(request,username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render (request,'loginpage.html')

@login_required(login_url='login')
def homepage(request):
    # return HttpResponse("Hello world!")
    return render (request,'FE-MainPage.html')

@login_required(login_url='login')
def YourFess(request):
    history = {}
    if request.user.is_authenticated:
        user = request.user.username
        history = Post.objects.all().filter(user=user)
    return render (request, 'YourFess.html',{
        'history' : history,
    })

def Logout(request):
    logout(request)
    return redirect('login')
    