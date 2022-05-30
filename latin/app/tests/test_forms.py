from django.contrib.auth.models import User
from django.test import TestCase
import tempfile
from django.urls import reverse
from app.models import Country
from app.forms import CountryForm


class TestCountryForm(TestCase):

    def test_empty_form(self):
        form = CountryForm()
        self.assertInHTML('<input type="text" name="name" maxlength="100" required id="id_name">', str(form))
        self.assertInHTML('<input type="text" name="capital" maxlength="100" required id="id_capital">', str(form))

        self.assertIn('slug', form.fields)
        self.assertIn('population', form.fields)

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

    def SetUp(self):
        image = tempfile.NamedTemporaryFile(suffix='.jpg').name

        self.first_country = Country.objects.create(name='Russia', population=144100000.0, description='test1',
                                                    capital='Moscow', photos=image)

    def test_field1_should_change(self):
        image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        first_country = Country.objects.create(name='Russia', population=144100000.0, description='test1',
                                               capital='Moscow')
        response = self.client.post(
            reverse('detail', kwargs={'pk': first_country.id}),
            {'name': 'Russia',
             'population': 144100000.0,
             'description': 'test1',
             'capital': 'Moscow',
             'photos': image,
             }
        )
        self.assertEqual(response.status_code, 302)  # 405
        first_country.refresh_from_db()
        self.assertEqual(first_country.name, 'Russian')


class UserTestCase(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('login'))
        self.assertRedirects(resp, 'login')

    def test_logged_in_uses_incorrect_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('index'))

        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 302)
