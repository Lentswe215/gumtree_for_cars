# Generated by Django 3.0.6 on 2020-07-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsforsale', '0003_auto_20200711_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsforsale',
            name='delearship',
            field=models.CharField(default='', max_length=50),
        ),
    ]
