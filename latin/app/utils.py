from .models import Country, Region
from .forms import CountryForm


class MixinData:
    model = Country
    form_class = CountryForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['regions'] = Region.objects.all()
        return context
