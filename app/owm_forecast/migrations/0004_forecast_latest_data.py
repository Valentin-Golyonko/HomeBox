# Generated by Django 3.1.7 on 2021-02-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owm_forecast', '0003_auto_20201219_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='latest_data',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]