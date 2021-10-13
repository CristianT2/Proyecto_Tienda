# Generated by Django 3.2.7 on 2021-09-13 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20210913_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 16, 27, 35, 835005), verbose_name='Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 16, 27, 35, 835005)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 16, 27, 35, 819364), verbose_name='Fecha de Nacimiento'),
        ),
    ]
