# Generated by Django 3.0.3 on 2020-02-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
