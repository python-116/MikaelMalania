"""
URL configuration for studentApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addbook/', views.add_book, name='addbook'),
    path('books/', views.book_list, name='book_list'),
    path('tv_show/', views.get_tv_show_details, name='tv_show_details'),
    path('reg_student/', views.reg_student, name='student_registration'),
    path('login_student/', views.student_login, name='student_login'),
    path('profile/', views.student_profile_page, name='student_profile'),

]