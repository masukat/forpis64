# Generated by Django 3.0.4 on 2020-06-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0038_wannado_plandate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habitflag',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
