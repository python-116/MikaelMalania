from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=100, default='abc')
    password = models.CharField(max_length=100, default='def')
    session_token = models.CharField(max_length=32, null=True, default=None)

    def __str__(self):
        return self.first_name

