# Generated by Django 4.2.6 on 2023-11-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_blog', '0008_articulo_imagen_delete_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/imagenes'),
        ),
    ]
