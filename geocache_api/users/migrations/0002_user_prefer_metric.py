# Generated by Django 3.2.13 on 2022-05-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prefer_metric',
            field=models.BooleanField(blank=True, default=False, verbose_name='Prefers metric measurements'),
        ),
    ]