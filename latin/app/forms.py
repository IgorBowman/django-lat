from django.forms import ModelForm

from .models import Country
from captcha.fields import CaptchaField


class CountryForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Country
        fields = ("name", "slug", "population", "description", "capital",
                  "photos", "lang", "religion", "politic", "reg",)
