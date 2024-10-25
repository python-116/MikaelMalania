from django.shortcuts import render, redirect
from .models import Book
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add_book(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        publication_date = request.POST.get('publication_date')

        Book.objects.create(name=book_name, author=author_name,
                            publication_year=publication_date)

        return redirect('index')

    return render(request, 'addbook.html')


def book_list(request):
    books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})
