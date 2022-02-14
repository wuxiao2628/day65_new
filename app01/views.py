from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models

# Create your views here.


def home(request):
    return render(request, 'home.html', locals())


def book_list(request):
    book_obj = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def author_list(request):
    author_obj = models.Author.objects.all()
    return render(request, 'author_list.html', locals())


def publish_list(request):
    if request.method == 'POST':
        pk = request.POST.get('publish_id')
        name = request.POST.get('publish_name')
        address = request.POST.get('publish_address')
        email = request.POST.get('publish_email')
        if request.POST.get('edit_publish_form') == 'True':  # from 表单有多个，通过传递提交按钮携带的值判断来自哪个form表单然后判断处理
            models.Publish.objects.filter(pk=pk).update(name=name, addr=address, email=email)
        else:
            models.Publish.objects.create(name=name, addr=address, email=email)
    publish_queryset = models.Publish.objects.all()
    # print(publish_queryset)
    return render(request, 'publish_list.html', locals())
