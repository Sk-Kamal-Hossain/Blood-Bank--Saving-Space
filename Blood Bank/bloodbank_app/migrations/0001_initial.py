# Generated by Django 3.1.4 on 2020-12-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('bloodgroup', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('passwordr', models.CharField(max_length=20)),
            ],
        ),
    ]