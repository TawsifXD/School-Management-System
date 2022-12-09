from django.shortcuts import render,redirect

def BASE(request):
    return render (request, 'base.html')

def LOGIN(request):
    return render (request, 'login.html')
