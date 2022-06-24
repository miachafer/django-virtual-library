from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('books/', views.books, name='books'),
    path('books/register-a-book/', views.books_register, name='books_register'),
    path('logout/', views.logout, name='logout'),
]
