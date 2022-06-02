from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.base import View

from .models import *
from .forms import CountryForm, RegisterUserForm, LoginUserForm


class CountrylistView(ListView):
    paginate_by = 1
    model = Country
    template_name = 'app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Country.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CountrylistView, self).get_context_data(**kwargs)
        context.update({
            'posts': Country.objects.all(),
            'regions': Region.objects.all()
        })
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


class CountryCreateView(LoginRequiredMixin, CreateView):
    form_class = CountryForm
    template_name = 'app/create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        return context


# def add_and_save(request):
#     """ Функция для создания новой записи"""
#
#     if request.method == 'POST':
#         cntry = CountryForm(request.POST)
#         if cntry.is_valid():
#             cntry.save()
#             return HttpResponseRedirect(reverse('app:show_cat',
#                                                 kwargs={'show_cat': cntry.cleaned_data['regions'].pk}))
#
#         else:
#             context = {'form': cntry}
#             return render(request, 'app/create.html', context)
#
#     else:
#         cntry = CountryForm()
#         context = {'form': cntry}
#         return render(request, 'app/create.html', context)


class CountryDetailView(View):
    """ Класс для просмотра записи"""

    def get(self, request, pk):
        country = Country.objects.get(id=pk)
        photos = CountryShots.objects.all().prefetch_related('countryshots_set')
        context = {'country': country,
                   'photos': photos}
        return render(request, 'app/country_detail.html', context)


class CountryEditView(LoginRequiredMixin, UpdateView):
    """ Класс редактирования записи"""

    model = Country
    form_class = CountryForm

    def get_success_url(self):
        country_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={'pk': country_id})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['regions'] = Region.objects.all()
        return context


class CountryDeleteView(LoginRequiredMixin, DeleteView):
    model = Country
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['regions'] = Region.objects.all()
        return context


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
