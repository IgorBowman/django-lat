from django.forms import ModelForm

from .models import Country


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'slug', 'population', 'description', 'capital',
                  'photos', 'lang', 'religion', 'politic', 'reg')


