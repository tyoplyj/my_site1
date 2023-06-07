# Generated by Django 4.2.1 on 2023-05-27 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='category_photos/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PerimetrShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('param', models.TextField(blank=True, verbose_name='Характеристики')),
                ('contents', models.TextField(blank=True, verbose_name='Обзор товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='perimetr_yug.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазин',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]