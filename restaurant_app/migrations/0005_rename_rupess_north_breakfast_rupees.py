# Generated by Django 3.2.2 on 2021-05-25 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0004_north_breakfast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='north_breakfast',
            old_name='rupess',
            new_name='rupees',
        ),
    ]
