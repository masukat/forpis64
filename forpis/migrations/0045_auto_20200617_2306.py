# Generated by Django 3.0.4 on 2020-06-17 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0044_auto_20200617_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wannado',
            name='plandate',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
