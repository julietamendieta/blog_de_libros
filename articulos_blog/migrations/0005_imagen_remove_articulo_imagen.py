# Generated by Django 4.2.6 on 2023-11-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_blog', '0004_articulo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_articulos')),
            ],
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='imagen',
        ),
    ]
