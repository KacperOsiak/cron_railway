from django.contrib import admin
from .models import Book, Joke
# Register your models here.

for i in [Book,Joke]:
    admin.site.register(i)