# Generated by Django 3.2.7 on 2021-09-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_booksmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='isAvailable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]