# Generated by Django 3.1.4 on 2020-12-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201206_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='i2c_address',
            field=models.CharField(default='', max_length=5, null=True, verbose_name='I2C address'),
        ),
    ]
