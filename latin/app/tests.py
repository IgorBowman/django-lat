from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
import tempfile

from django.urls import reverse

from .models import Country
from .forms import CountryForm


class PriceOutputTestCase(TestCase):

    def setUp(self):
        self.first_country_positive = Country.objects.create(name='Russia', population=144100000.0, description='test1',
                                                             capital='Moscow')
        self.first_country_negative = Country.objects.create(name='French', population=67390000.0, description='test2',
                                                             capital='Paris')
        self.second_country_positive = Country.objects.create(name='Turkey', population=84340000.0, description='test3',
                                                              capital='Ankara')
        self.second_country_negative = Country.objects.create(name='England', population=55980000.0,
                                                              description='test4', capital='London')

    def test_one_positive(self):
        self.assertEqual(144.1, self.first_country_positive.correct_view_population())

    def test_one_negative(self):
        self.assertNotEqual(67.4, self.first_country_negative.correct_view_population())

    def test_two_positive(self):
        self.assertEqual(84.34, self.second_country_positive.correct_view_population())

    def test_two_negative(self):
        self.assertNotEqual(55.99, self.second_country_negative.correct_view_population())


class TestCountryForm(TestCase):

    def test_empty_form(self):
        form = CountryForm()
        self.assertInHTML('<input type="text" name="name" maxlength="100" required id="id_name">', str(form))
        self.assertInHTML('<input type="text" name="capital" maxlength="100" required id="id_capital">', str(form))

        self.assertIn("slug", form.fields)
        self.assertIn("population", form.fields)

    def test_create_valid_form(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        form = CountryForm(data={
            'name': 'Russia',
            'slug': 'russia',
            'population': 1441000000.0,
            'capital': 'Moscow',
            'photos': image,
            'lang': 'russian',
            'religion': 'christians',
            'politic': 'authorian',
            'reg': 'East Europe',

        })
        self.assertTrue(form.is_valid())
        # self.assertFalse(form.is_valid())


class TestEditForm(TestCase):

    # def SetUp(self):
    #     image = tempfile.NamedTemporaryFile(suffix=".jpg").name
    #
    #     self.first_country = Country.objects.create(name='Russia', population=144100000.0, description='test1',
    #                                                          capital='Moscow', photos=image)

    def test_field1_should_change(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        first_country = Country.objects.create(name='Russia', population=144100000.0, description='test1',
                                               capital='Moscow')
        response = self.client.post(
            reverse('detail', kwargs={'pk': first_country.id}),
            {'name': 'Russia',
             'population': 144100000.0,
             'description': 'test1',
             'capital': 'Moscow',
             }
        )
        self.assertEqual(response.status_code, 302)  # 405

        # return reverse_lazy('detail', kwargs={'pk': country_id})
        first_country.refresh_from_db()
        self.assertEqual(first_country.name, 'Russian')
