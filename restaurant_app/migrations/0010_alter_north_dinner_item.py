# Generated by Django 3.2.2 on 2021-05-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0009_north_dinner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='north_dinner',
            name='item',
            field=models.CharField(max_length=25),
        ),
    ]