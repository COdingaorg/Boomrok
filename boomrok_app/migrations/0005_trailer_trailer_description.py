# Generated by Django 3.2.6 on 2021-11-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boomrok_app', '0004_remove_trailer_trailer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='trailer_description',
            field=models.TextField(default='Trailer Description goes here'),
            preserve_default=False,
        ),
    ]
