# Generated by Django 3.2.4 on 2021-06-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bed'), (3, 'Not bad'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
