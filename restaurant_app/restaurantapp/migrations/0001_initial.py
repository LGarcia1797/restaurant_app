# Generated by Django 3.0.14 on 2022-10-28 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Npersonas', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(1)])),
                ('telefono', models.IntegerField()),
                ('diareserva', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(1, 'RESERVADO'), (2, 'COMPLETADO'), (3, 'ANULADO'), (4, 'NO ASISTEN')], default=1)),
                ('observacion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
