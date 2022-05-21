from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import CountryForm


def index(request):
    posts = Country.objects.all()
    regions = Region.objects.all()

    context = {
        'title': 'Главная страница',
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


class CountryCreateView(CreateView):
    form_class = CountryForm
    template_name = 'app/create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        return context

