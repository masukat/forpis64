# Generated by Django 3.0.4 on 2020-06-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0030_auto_20200609_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
