# Generated by Django 4.2.1 on 2023-06-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='car_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carros',
            name='RENAVAM',
            field=models.IntegerField(),
        ),
    ]