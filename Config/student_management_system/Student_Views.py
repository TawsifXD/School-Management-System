from django.shortcuts import render,redirect

def HOME(request):
    return render(request, 'Student/home.html')