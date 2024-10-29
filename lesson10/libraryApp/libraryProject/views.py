from django.shortcuts import render, redirect
from .models import Book
import asyncio
import aiohttp
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


async def tv_shows_api(tv_show_name):
    tv_show_api = f'https://api.tvmaze.com/search/shows?q={tv_show_name}'

    async with aiohttp.ClientSession() as session:
        async with session.get(tv_show_api) as response:
            data = await response.json()
            return data


async def get_tv_show_details(request):
    if request.method == "POST":
        show_name = request.POST.get('show_name')

        tv_shows = await tv_shows_api(show_name)

        if len(tv_shows) == 0:
            return render(request, 'tv_shows.html', {'found_show': False})

        imdb_score = tv_shows[0]['score']
        official_site = tv_shows[0]['show']['url']
        image = tv_shows[0]['show']['image']['medium']
        summary = tv_shows[0]['show']['summary']

        return render(request, 'tv_shows.html', {'found_show': True, 'imdb_score': imdb_score, 'official_site': official_site, 'image': image, 'summary': summary})
    else:
        return render(request, 'tv_shows.html')
