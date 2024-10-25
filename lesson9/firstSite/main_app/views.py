from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def about(request):
    coworkers_db = [
        {
            "first_name": "John",
            "last_name": "Johnson",
            "profession": "Manager",
            "salary": "1000$",
        },
        {
            "first_name": "Jack",
            "last_name": "Jackson",
            "profession": "Developer",
            "salary": "800$",
        },
        {
            "first_name": "Jane",
            "last_name": "Janeway",
            "profession": "Developer",
            "salary": "800$",
        },
        {
            "first_name": "Joan",
            "last_name": "Joanson",
            "profession": "Analyst",
            "salary": "900$",
        },
        {
            "first_name": "Jill",
            "last_name": "Jillson",
            "profession": "Tester",
            "salary": "700$",
        },
    ]

    return render(request, './about.html', {'coworkers': coworkers_db})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()

    return render(request, './contactPage.html', {'form': form})


def view_contact_data(request):
    contacts = Contact.objects.all()
    return render(request, './getContacts.html', {'contacts': contacts})
