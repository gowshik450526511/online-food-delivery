# Generated by Django 3.2.2 on 2021-05-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0006_north_lunch'),
    ]

    operations = [
        migrations.CreateModel(
            name='south_lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='media/media/pics')),
                ('rupees', models.IntegerField()),
            ],
        ),
    ]
