# Generated by Django 3.0.4 on 2020-06-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0025_auto_20200604_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relate_get',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('getgenre1', models.CharField(blank=True, max_length=100)),
                ('get', models.TextField(blank=True)),
                ('getdate', models.DateField(blank=True)),
                ('geturllink', models.TextField(blank=True)),
                ('getmemo', models.TextField(blank=True)),
                ('getreview', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'relate_get',
            },
        ),
        migrations.CreateModel(
            name='Relate_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plangenre1', models.CharField(blank=True, max_length=100)),
                ('plan', models.TextField(blank=True)),
                ('plandate', models.DateField(blank=True)),
                ('planurllink', models.TextField(blank=True)),
                ('planmemo', models.TextField(blank=True)),
                ('done', models.BooleanField()),
                ('planreview', models.IntegerField(blank=True)),
                ('motivation', models.IntegerField(blank=True)),
                ('completiondate', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'relate_plan',
            },
        ),
        migrations.DeleteModel(
            name='Relate',
        ),
    ]
