# Generated by Django 2.1.7 on 2019-03-07 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_remove_emp_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 5, 4, 53, 443593, tzinfo=utc)),
        ),
    ]