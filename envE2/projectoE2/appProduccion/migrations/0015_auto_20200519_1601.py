# Generated by Django 3.0.4 on 2020-05-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduccion', '0014_auto_20200519_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedades',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
