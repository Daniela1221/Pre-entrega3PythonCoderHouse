# Generated by Django 4.2.3 on 2023-07-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subscripción',
                'verbose_name_plural': 'Subscripciones',
            },
        ),
    ]
