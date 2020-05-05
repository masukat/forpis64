# Generated by Django 3.0.4 on 2020-05-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0008_auto_20200501_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressHabit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.IntegerField(blank=True)),
                ('frequency', models.IntegerField(blank=True)),
                ('division', models.IntegerField(blank=True)),
                ('number', models.IntegerField(blank=True)),
                ('genre1', models.CharField(max_length=100)),
                ('habit', models.TextField()),
                ('memo', models.TextField(blank=True)),
                ('done1', models.BooleanField(blank=True)),
                ('done2', models.BooleanField(blank=True)),
                ('done3', models.BooleanField(blank=True)),
                ('done4', models.BooleanField(blank=True)),
                ('review', models.IntegerField(blank=True)),
                ('completiondate', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'habit',
            },
        ),
        migrations.CreateModel(
            name='ProgressHabit_motivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.IntegerField(blank=True, choices=[('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')])),
            ],
        ),
        migrations.CreateModel(
            name='ProgressStressrelief_motivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.IntegerField(blank=True, choices=[('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')])),
            ],
        ),
    ]