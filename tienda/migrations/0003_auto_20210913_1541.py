# Generated by Django 3.2.7 on 2021-09-13 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20210912_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['movimiento', 'articulo']},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 15, 41, 55, 64939), verbose_name='Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 15, 41, 55, 64939)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(default=datetime.datetime(2021, 9, 13, 15, 41, 55, 64939), verbose_name='Fecha de Nacimiento'),
        ),
    ]
