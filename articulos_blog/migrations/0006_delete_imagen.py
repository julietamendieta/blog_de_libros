# Generated by Django 4.2.6 on 2023-11-18 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_blog', '0005_imagen_remove_articulo_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
