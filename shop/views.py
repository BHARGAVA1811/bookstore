from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'shop/index.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'shop/book_detail.html', {'book': book})
