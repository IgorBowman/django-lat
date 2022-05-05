from django.shortcuts import render

from .models import *


def index(request):
    context = Country.objects.all()
    return render(request, 'app/index.html', context=context)
