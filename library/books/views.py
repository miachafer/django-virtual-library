from django.shortcuts import render
from django.http import request

def home(request):
    return render(request, 'books/home.html')

def register(request):
    return render(request, 'books/register.html')

def login(request):
    return render(request, 'books/login.html')
