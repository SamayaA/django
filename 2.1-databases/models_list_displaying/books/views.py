from django.db.models.fields import DateField
from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, template, context)

def book_view(request, pub_date: DateField):
    template = 'books/books_list.html'
    books = [Book.objects.get(pub_date=pub_date)]
    context = {
        "books": books,
    }
    return render(request, template, context)
