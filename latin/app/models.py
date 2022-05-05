from django.db import models

REG_CHOICES = (
    ('caribs', 'caribs'),
    ('mexico', 'mexico'),
    ('central', 'central'),
    ('north', 'central'),
    ('south', 'south'),
)


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    population = models.FloatField(verbose_name='Население')
    description = models.TextField(verbose_name='Описание')
    capital = models.CharField(max_length=100, verbose_name='Столица')
    photos = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    lang = models.ForeignKey('Religion', on_delete=models.PROTECT, null=True, verbose_name='Язык', related_name='country_language')
    religion = models.ForeignKey('Religion', on_delete=models.PROTECT, null=True, verbose_name='Религия', related_name='country_religion')
    politic = models.ForeignKey('Politition', on_delete=models.PROTECT, null=True, verbose_name='Политическая система')
    reg = models.ForeignKey('Region', on_delete=models.PROTECT, null=True, verbose_name='Регион')

    anphoto = models.ForeignKey('AnotherPhoto', on_delete=models.PROTECT, null=True, verbose_name='Другие фото')


    def __str__(self):
        return self.name, self.lang


class Region(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Регион')

    def __str__(self):
        return self.name


class Politition(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Политическая система')

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Политическая система')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Политическая система')

    def __str__(self):
        return self.name


# expirement
class AnotherPhoto(models.Model):
    image = models.ImageField('Изображения', upload_to='pictures/')

    # def __str__(self):
    #     return self.name


