# Generated by Django 2.2.3 on 2022-10-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('idServicioOfrecido', models.AutoField(primary_key=True, serialize=False)),
                ('servicioOfrecidoNombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('servicioOfrecidoDesripcion', models.CharField(max_length=125, verbose_name='Descripción')),
                ('servicioOfrecidoActivo', models.CharField(max_length=1, verbose_name='Estado')),
            ],
        ),
    ]
