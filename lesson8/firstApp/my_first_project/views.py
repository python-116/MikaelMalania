from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse(
#         """
#         <html>
#             <head>
#                 <title>My First Django App</title>
#             </head>

#             <body>
#                 <h1>Hello, world. You're at the index page.</h1>
#             </body>

#             <footer>
#                 <p>This is a footer.</p>
#             </footer>

#             <script>
#                 alert('This is an alert message!');
#                 console.log('This is a console log.');
#             </script>
#         </html>
#         """
#     )

def index(request):
    successful_projects = [
        {
            'name': 'Project A',
            'description': 'A successful project that resulted in increased sales.',
            'year': 2020
        },
        {
            'name': 'Project B',
            'description': 'A challenging project that required careful planning and execution.',
            'year': 2021
        },
        {
            'name': 'Project C',
            'description': 'A project that was awarded a prestigious award.',
            'year': 2022
        }
    ]

    return render(request, './index.html', {'projects': successful_projects, 'current_year': 2024})


def about(request):
    coworkers = [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'position': 'Software Engineer'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'position': 'Product Manager'
        },
        {
            'first_name': 'Michael',
            'last_name': 'Johnson',
            'position': 'Senior Software Engineer'
        },
        {
            'first_name': 'Emily',
            'last_name': 'Williams',
            'position': 'Data Scientist'
        },
        {
            'first_name': 'David',
            'last_name': 'Brown',
            'position': 'UX/UI Designer'
        }
    ]

    return render(request, './about.html', {'coworkers': coworkers})
