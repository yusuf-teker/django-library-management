# Generated by Django 3.2.7 on 2021-09-04 19:54

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='bookName', unique=True)),
                ('bookBlurb', models.TextField()),
                ('coverPicture', models.ImageField(upload_to='book_cover_picture')),
                ('author', models.CharField(max_length=30)),
                ('numberOfPages', models.IntegerField()),
                ('publicationYear', models.DateField()),
                ('categories', models.ManyToManyField(related_name='book', to='library.CategoriesModel')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
