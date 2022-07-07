# Generated by Django 4.0.4 on 2022-05-30 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_cityweather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='app.countryshots', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='country',
            name='politic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='politic', to='app.politition', verbose_name='Политическая система'),
        ),
        migrations.AlterField(
            model_name='country',
            name='reg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='region', to='app.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, verbose_name='URL'),
        ),
    ]
