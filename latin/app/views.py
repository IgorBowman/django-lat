from django.shortcuts import render

from .models import *


def index(request):
    posts = Country.objects.all()
    cat = Region.objects.all()
    context = {
        'posts': posts,
        'cat': cat,
    }
    return render(request, 'app/index.html', context=context)


# def show_category(request, pk):
#     posts = Region.objects.filter(pk=pk)
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'app/index.html', context=context)
