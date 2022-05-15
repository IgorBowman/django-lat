from django.shortcuts import render

from .models import *


def index(request):
    posts = Country.objects.all()
    regions = Region.objects.all()
    context = {
        'posts': posts,
        'regions': regions,
    }
    return render(request, 'app/index.html', context)


def show_category(request, pk):
    posts = Country.objects.filter(reg_id=pk)
    regions = Region.objects.all()
    current_reg = Region.objects.get(id=pk)
    context = {
        'posts': posts,
        'regions': regions,
        'current_reg': current_reg,
    }
    return render(request, 'app/show_category.html', context)
