from django.shortcuts import render, get_object_or_404

from .models import Book, Author

def home(request):
    books = Book.objects
    return render(request, 'books/home.html', {'books':books})

def about(request):
    return render(request, 'books/about.html')


def detail(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book':book_detail})
