# Generated by Django 3.2.7 on 2021-10-07 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_auto_20211007_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='articulos/'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2021, 10, 7, 18, 7, 11, 854591), verbose_name='Fecha de Alta'),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 10, 7, 18, 7, 11, 854591)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(default=datetime.datetime(2021, 10, 7, 18, 7, 11, 854591), verbose_name='Fecha de Nacimiento'),
        ),
    ]
