# Generated by Django 3.0.4 on 2020-05-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0015_auto_20200504_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progresshabit_division',
            name='division',
            field=models.CharField(blank=True, choices=[('やめたい', 'やめたい'), ('朝', '朝'), ('昼', '昼'), ('夜', '夜'), ('月', '月'), ('火', '火'), ('水', '水'), ('木', '木'), ('金', '金')], max_length=100),
        ),
        migrations.AlterField(
            model_name='progresshabit_frequency',
            name='frequency',
            field=models.IntegerField(blank=True, choices=[('0', '毎日'), ('1', '毎週'), ('2', '毎月')]),
        ),
    ]
