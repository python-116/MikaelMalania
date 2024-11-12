from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Student
import aiohttp
from random_strings import random_string
from django.contrib.auth.hashers import make_password, check_password
import secrets
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

    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(tv_show_api) as response:
            data = await response.json()
            return data


def reg_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        hashed_password = make_password(password)

        Student.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date, address=address,
                               phone_number=phone_number, email=email, username=username, password=hashed_password)
        return HttpResponse(
            f'''
            <h3>Congrats! you have successfully registered!! </h3>
            <p> Your username is: {username} </p>
            <p> Your password is: {password} </p>
        '''
        )

    else:
        return render(request, 'reg_student.html')


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


def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        db_password = Student.objects.filter(
            username=username).values('password').first()

        if db_password is not None and check_password(password, db_password['password']):
            session_token = secrets.token_hex(32)
            request.session['session_token'] = session_token
            Student.objects.filter(username=username).update(
                session_token=session_token)
            return redirect('student_profile')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid username or password'})
        # return redirect('index')

    else:
        return render(request, 'student_login.html')


def student_profile_page(request):
    session_token = request.session.get('session_token')
    print(session_token)
    if session_token:
        student = Student.objects.filter(
            session_token=session_token).values().first()
        student.pop('password')
        student.pop('session_token')
        student.pop('id')

        return render(request, 'student_profile.html', {'student_data': student})
    else:
        return render(request, 'student_profile.html', {'student_data': False})
