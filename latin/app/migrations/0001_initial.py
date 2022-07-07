# Generated by Django 4.0.4 on 2022-05-05 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/', verbose_name='Изображения')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Политическая система')),
            ],
        ),
        migrations.CreateModel(
            name='Politition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Политическая система')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Политическая система')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('population', models.FloatField(verbose_name='Население')),
                ('description', models.TextField(verbose_name='Описание')),
                ('capital', models.CharField(max_length=100, verbose_name='Столица')),
                ('photos', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('anphoto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.anotherphoto', verbose_name='Другие фото')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='country_language', to='app.religion', verbose_name='Язык')),
                ('politic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.politition', verbose_name='Политическая система')),
                ('reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.region', verbose_name='Регион')),
                ('religion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='country_religion', to='app.religion', verbose_name='Религия')),
            ],
        ),
    ]