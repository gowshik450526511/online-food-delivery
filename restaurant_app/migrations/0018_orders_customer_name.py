# Generated by Django 3.2.2 on 2021-06-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0017_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer_name',
            field=models.CharField(default='true', max_length=40),
        ),
    ]