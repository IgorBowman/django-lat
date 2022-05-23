from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.views.generic.base import View ## delete

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


class CountryRegionView(TemplateView):
    template_name = 'app/show_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Country.objects.filter(reg_id=context['pk'])
        context['regions'] = Region.objects.all()
        context['current_reg'] = Region.objects.get(pk=context['pk'])

        return context


# class CountryCreateView(CreateView):
#     form_class = CountryForm
#     template_name = 'app/create.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['regions'] = Region.objects.all()
#         return context

def add_and_save(request):
    if request.method == 'POST':
        cntry = CountryForm(request.POST)
        if cntry.is_valid():
            cntry.save()
            return HttpResponseRedirect(reverse('app:show_cat',
                                                kwargs={'show_cat': cntry.cleaned_data['regions'].pk}))

        else:
            context = {'form': cntry}
            return render(request, 'app/create.html', context)

    else:
        cntry = CountryForm()
        context = {'form': cntry}
        return render(request, 'app/create.html', context)


# class CountryDetailView(DetailView):
#     model = Country
    ##templates_name = 'app/country_detail.html'
    ##queryset = Country.objects.filterl(id__gt=pk)

    #context_object_name = 'country'

#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #context['regions'] = Region.objects.all()  # 'reg'
#         context['regs'] = Region.objects.all()  # 'reg'
#         return context

###fajfajfhaf
        # def get_object(self, queryset=None):
        #     slug = self.kwargs.get(self.slug_url_kwarg, None)
        #     try:
        #         return queryset.get(slug=slug)
        #     except PostDoesNotExist:
        #         raise Http404('Ох, нет объекта;)')

class CountryDetailView(View):

    def get(self, request, pk):
        country = Country.objects.get(id=pk)
        return render(request, "app/country_detail.html", {'country': country})
