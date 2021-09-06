# Generated by Django 3.2.7 on 2021-09-05 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0003_booksmodel_isavailable'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='lendby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booksmodel',
            name='lendperiod',
            field=models.DateField(blank=True, null=True),
        ),
    ]
