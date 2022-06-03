from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.base import View

from .models import Country, Region, CountryShots
from .forms import RegisterUserForm, LoginUserForm

from .utils import MixinData


class CountrylistView(MixinData, ListView):
    paginate_by = 1
    template_name = 'app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Country.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Country.objects.all()
        context['regions'] = Region.objects.all()

        return context


class CountryRegionView(TemplateView):
    """Сортировка по региону"""

    template_name = 'app/show_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Country.objects.filter(reg_id=context['pk'])
        context['regions'] = Region.objects.all()
        context['current_reg'] = Region.objects.get(pk=context['pk'])

        return context


class CountryCreateView(MixinData, LoginRequiredMixin, CreateView):
    template_name = 'app/create.html'
    success_url = reverse_lazy('home')


class CountryDetailView(View):
    """ Класс для просмотра записи"""

    def get(self, request, pk):
        country = Country.objects.get(id=pk)
        photos = CountryShots.objects.all().prefetch_related('countryshots_set')
        context = {'country': country,
                   'photos': photos}
        return render(request, 'app/country_detail.html', context)


class CountryEditView(MixinData, LoginRequiredMixin, UpdateView):
    """ Класс редактирования записи"""

    def get_success_url(self):
        country_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={'pk': country_id})


class CountryDeleteView(MixinData, LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
