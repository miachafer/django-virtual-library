from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.http import HttpResponse
from .models import Book

def home(request):
    return render(request, 'books/home.html')

def register(request):
    if request.method == "GET":
        return render(request, 'books/register.html')
    else:
        username = request.POST.get("username")
        user_email = request.POST.get("user_email")
        password = request.POST.get("password")
        # The following variable searches in database to check if this user already exists.
        user = User.objects.filter(username=username).first()
        if user:
            context = {
                "message": "This user already exists."
            }
            return render (request, 'books/register.html', context)
        new_user = User.objects.create_user(username=username, email=user_email, password=password)
        new_user.save()
        context = {
                "message": "User registered successfully!"
            }
        return render (request, 'books/register.html', context)        

def login(request):
    if request.method == "GET":
        return render(request, 'books/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if(user):
            do_login(request, user)
            return redirect("books")
        else:
            context = {
                "message": "Wrong username or password. Try again."
            }
            return render(request, 'books/login.html', context)

def books(request):
    list_of_books = Book.objects.all()
    context = {
        "books": list_of_books
        }
    return render(request, "books/books.html", context)

def books_register(request):
    if request.method == "GET":
        return render(request, "books/books_register.html")
    else:
        book_name = request.POST.get("book_name")
        author_name = request.POST.get("author_name")
        release_date = request.POST.get("release_date")
        book_synopsis = request.POST.get("book_synopsis")
        book = Book.objects.filter(name=book_name).first()
        if book:
            context = {
                "message": "This book is already registered."
            }
            return render (request, "books/books_register.html", context)
        else: 
            book = Book.objects.create(name=book_name, author=author_name, release_date=release_date, synopsis=book_synopsis)
            book.save()
            context = {
                "message": f"The book {book_name} was registered successfully."
            }
            return render (request, "books/books_register.html", context)
