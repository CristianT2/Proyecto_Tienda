# Generated by Django 3.2.7 on 2021-09-23 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_auto_20210922_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2021, 9, 23, 15, 21, 57, 871902), verbose_name='Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='cp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 9, 23, 15, 21, 57, 887545)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(default=datetime.datetime(2021, 9, 23, 15, 21, 57, 871902), verbose_name='Fecha de Nacimiento'),
        ),
    ]
