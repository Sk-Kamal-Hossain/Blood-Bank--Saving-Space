# Generated by Django 3.1.4 on 2021-01-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_app', '0004_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='phone',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
