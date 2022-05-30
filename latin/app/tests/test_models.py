from django.test import TestCase

from app.models import Country, Region, Politition, Religion, Language


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

    def test_return_correct_name_country(self):
        name_exist = self.first_country_positive
        self.assertTrue(isinstance(name_exist, Country))
        self.assertEqual(name_exist.__str__(), name_exist.name)

    def test_one_positive(self):
        self.assertEqual(144.1, self.first_country_positive.correct_view_population())

    def test_one_negative(self):
        self.assertNotEqual(67.4, self.first_country_negative.correct_view_population())

    def test_two_positive(self):
        self.assertEqual(84.34, self.second_country_positive.correct_view_population())

    def test_two_negative(self):
        self.assertNotEqual(55.99, self.second_country_negative.correct_view_population())


class RegionTestCase(TestCase):

    def create_region_model(self, name='Europe', slug='europe'):
        return Region.objects.create(name=name, slug=slug)

    def test_return_correct_name_region(self):
        name_exist = self.create_region_model()
        self.assertTrue(isinstance(name_exist, Region))
        self.assertEqual(name_exist.__str__(), name_exist.name)

    def test_return_slug(self):
        name_exist = self.create_region_model()
        self.assertTrue(isinstance(name_exist, Region))
        self.assertEqual(name_exist.get_absolute_url(), '/app/2/')


class PolititionTestCase(TestCase):

    def create_politition_model(self, name='Democracy'):
        return Politition.objects.create(name=name)

    def test_return_correct_name_region(self):
        name_exist = self.create_politition_model()
        self.assertTrue(isinstance(name_exist, Politition))
        self.assertEqual(name_exist.__str__(), name_exist.name)


class ReligionTestCase(TestCase):

    def create_religion_model(self, name='Budism'):
        return Religion.objects.create(name=name)

    def test_return_correct_name_region(self):
        name_exist = self.create_religion_model()
        self.assertTrue(isinstance(name_exist, Religion))
        self.assertEqual(name_exist.__str__(), name_exist.name)


class LanguageTestCase(TestCase):

    def create_language_model(self, name='English'):
        return Language.objects.create(name=name)

    def test_return_correct_name_region_model(self):
        name_exist = self.create_language_model()
        self.assertTrue(isinstance(name_exist, Language))
        self.assertEqual(name_exist.__str__(), name_exist.name)
