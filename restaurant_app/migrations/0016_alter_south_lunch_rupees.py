# Generated by Django 3.2.2 on 2021-06-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0015_alter_south_lunch_rupees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='south_lunch',
            name='rupees',
            field=models.IntegerField(),
        ),
    ]
