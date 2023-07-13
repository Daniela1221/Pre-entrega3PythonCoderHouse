# Generated by Django 4.2.3 on 2023-07-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion_url', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(max_length=250)),
            ],
        ),
    ]