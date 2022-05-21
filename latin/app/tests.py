from django.test import TestCase

from .models import Country


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
