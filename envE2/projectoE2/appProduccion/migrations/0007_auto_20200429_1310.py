# Generated by Django 3.0.4 on 2020-04-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduccion', '0006_auto_20200429_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
