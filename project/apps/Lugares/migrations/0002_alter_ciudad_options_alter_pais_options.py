# Generated by Django 4.2.3 on 2023-07-12 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lugares', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'País', 'verbose_name_plural': 'Países'},
        ),
    ]
