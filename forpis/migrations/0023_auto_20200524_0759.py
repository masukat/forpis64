# Generated by Django 3.0.4 on 2020-05-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0022_auto_20200522_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wannado',
            name='plan',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wannado',
            name='tag1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wannado',
            name='tag2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wannado',
            name='tag3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wannado',
            name='urllink',
            field=models.TextField(blank=True),
        ),
    ]