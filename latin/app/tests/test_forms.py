from django.test import Client
from django.test import TestCase
import tempfile
from django.urls import reverse
from app.models import Country
from app.forms import CountryForm
from captcha.models import CaptchaStore


class TestCountryForm(TestCase):

    def test_empty_form(self):
        form = CountryForm()
        self.assertInHTML('<input type="text" name="name" maxlength="100" required id="id_name">', str(form))
        self.assertInHTML('<input type="text" name="capital" maxlength="100" required id="id_capital">', str(form))

        self.assertIn('slug', form.fields)
        self.assertIn('population', form.fields)

    def test_create_valid_form(self):
        captcha = CaptchaStore.objects.get(hashkey=CaptchaStore.generate_key())

        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        form = CountryForm(data={
            'name': 'Russia',
            'slug': 'russia',
            'population': 1441000000,
            'capital': 'Moscow',
            'photos': image,
            'lang': 'russian',
            'religion': 'christians',
            'politic': 'authorian',
            'reg': 'East Europe',
            'captcha': captcha,
            # 'captcha_0': captcha.hashkey,
            # 'captcha_1': captcha.response
        })

        captcha_count = CaptchaStore.objects.count()
        self.failUnlessEqual(captcha_count, 1)
        self.assertTrue(form.is_valid())


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


class BaseUserTests(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'password2': 'password',
            'name': 'fullname'
        }

    def test_can_view_page_correctly(self):
        response = self.guest_client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_get_add_page_client_user(self):
        response = self.guest_client.get('add/')
        self.assertEqual(response.status_code, 404)

    def test_can_register_user(self):
        response = self.guest_client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_can_access_page(self):
        response = self.guest_client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
