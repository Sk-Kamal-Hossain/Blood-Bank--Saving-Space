# Generated by Django 3.1.4 on 2021-01-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sendrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
