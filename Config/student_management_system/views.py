from django.shortcuts import render,redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def BASE(request):
    return render (request, 'base.html')

def LOGIN(request):
    return render (request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request, 'Email and password are Invalid!')
                return redirect('login')
        else: 
            messages.error(request, 'Email and password are Invalid!')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')
