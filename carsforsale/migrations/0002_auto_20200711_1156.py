# Generated by Django 3.0.6 on 2020-07-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsforsale',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]