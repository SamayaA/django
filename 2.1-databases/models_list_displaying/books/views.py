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
    books = list(Book.objects.all().order_by("pub_date"))
    length = len(books)
    pagination = Paginator(books, 1)
    current_page = books.index(Book.objects.get(pub_date=pub_date))+1
    page = pagination.get_page(current_page)
    list_dates = [date.pub_date for date in books]
    context = {
        "books": page.object_list,
        "page": page,
        "dates": list_dates,
    }
    return render(request, template, context)
