from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL",
                            null=True, blank=True)
    population = models.FloatField(verbose_name='Население')
    description = models.TextField(verbose_name='Описание')
    capital = models.CharField(max_length=100, verbose_name='Столица')
    photos = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    lang = models.ForeignKey('Language', on_delete=models.PROTECT, null=True,
                             verbose_name='Язык', related_name='country_language')
    religion = models.ForeignKey('Religion', on_delete=models.PROTECT, null=True,
                                 verbose_name='Религия', related_name='country_religion')
    politic = models.ForeignKey('Politition', on_delete=models.PROTECT, null=True,
                                verbose_name='Политическая система')
    reg = models.ForeignKey('Region', on_delete=models.PROTECT, null=True, verbose_name='Регион')
    images = models.ForeignKey('CountryShots', on_delete=models.CASCADE, verbose_name='Изображения',
                               null=True, blank=True)

    def correct_view_population(self):
        if len(str(self.population)) > 4:
            result = int(self.population) / 1000000
            return result

        return self.population

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('country', kwargs={'country_slug': self.slug})

    def get_absolute_url(self):
        return reverse('country', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Countries'


class Region(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Регион')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",
                            null=True, blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('show_cat', kwargs={'region_slug': self.slug})
    def get_absolute_url(self):
        return reverse('show_cat', kwargs={'pk': self.pk})


class Politition(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Политическая система')

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Религия')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Язык')

    def __str__(self):
        return self.name


class CountryShots(models.Model):
    country_name = models.ForeignKey(Country, verbose_name='Страна',
                                     on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='country_shots/%Y/%m/%d/')

    def __str__(self):
        return f"{self.country_name}_{self.id}"

    class Meta:
        verbose_name_plural = 'Country shots'

