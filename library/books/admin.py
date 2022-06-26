from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["author"]

admin.site.register(Book, BookAdmin)
