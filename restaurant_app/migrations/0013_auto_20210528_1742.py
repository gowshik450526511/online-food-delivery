# Generated by Django 3.2.2 on 2021-05-28 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0012_userprofileinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='north_breakfast',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='north_dinner',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='north_lunch',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='south_breakfast',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='south_dinner',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='south_lunch',
            old_name='item',
            new_name='name',
        ),
    ]
