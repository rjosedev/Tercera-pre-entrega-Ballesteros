# Generated by Django 5.0.6 on 2024-06-06 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('num_id', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('referente', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('num_id', models.IntegerField()),
                ('switchowner', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('num_id', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('rack', models.CharField(max_length=100)),
                ('sitio', models.CharField(max_length=100)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.proveedor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]