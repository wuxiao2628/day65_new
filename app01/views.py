from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models

# Create your views here.


def home(request):
    return render(request, 'home.html', locals())


def book_list(request):
    book_obj = models.Book.objects.all()
    print(book_obj)
    return render(request, 'book_list.html', locals())