# Generated by Django 3.0.4 on 2020-06-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forpis', '0024_relate_relate_motivation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relate',
            old_name='genre1',
            new_name='getgenre1',
        ),
        migrations.AddField(
            model_name='relate',
            name='plangenre1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]