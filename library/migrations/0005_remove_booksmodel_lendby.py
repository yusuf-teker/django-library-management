# Generated by Django 3.2.7 on 2021-09-06 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210905_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='lendby',
        ),
    ]
