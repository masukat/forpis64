from django.db import models

MOTIVATION_CHOISES=(
    ('6','6'),
    ('5','5'),
    ('4','4'),
    ('3','3'),
    ('2','2'),
    ('1','1'),
)

FREQUENCY_CHOISES=(
    ('0','やめたい'),
    ('1','毎日'),
    ('2','毎週'),
    ('3','毎月'),
)

DIVISION_CHOISES=(
    ('朝','朝'),
    ('昼','昼'),
    ('夜','夜'),
    ('月','月'),
    ('火','火'),
    ('水','水'),
    ('木','木'),
    ('金','金'),
)

class ProgressHabit_motivation(models.Model):
    motivation = models.IntegerField(blank=True,choices=MOTIVATION_CHOISES)

class ProgressHabit_frequency(models.Model):
    frequency = models.IntegerField(blank=True,choices=FREQUENCY_CHOISES)

class ProgressHabit_division(models.Model):
    division = models.CharField(blank=True,max_length=100,choices=DIVISION_CHOISES)

class ProgressHabit(models.Model):
    motivation = models.IntegerField(blank=True)
    frequency = models.IntegerField(blank=True)
    division = models.CharField(blank=True,max_length=100)
    number = models.IntegerField(blank=True)
    genre1 = models.CharField(max_length=100)
    habit = models.TextField()
    memo = models.TextField(blank=True)
    done1 = models.BooleanField(blank=True)
    done2 = models.BooleanField(blank=True)
    done3 = models.BooleanField(blank=True)
    done4 = models.BooleanField(blank=True)
    review = models.IntegerField(blank=True)
    completiondate = models.DateField(blank=True)

    class Meta:
        db_table ="habit"

# Create your models here.
