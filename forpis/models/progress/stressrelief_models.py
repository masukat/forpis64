from django.db import models

MOTIVATION_CHOISES=(
    ('6','6'),
    ('5','5'),
    ('4','4'),
    ('3','3'),
    ('2','2'),
    ('1','1'),
)

class ProgressStressrelief_motivation(models.Model):
    motivation = models.IntegerField(blank=True,choices=MOTIVATION_CHOISES)

class ProgressStressrelief(models.Model):
    genre1 = models.CharField(max_length=100)
    genre2 = models.CharField(max_length=100,blank=True)
    plan = models.TextField()
    urllink = models.TextField(blank=True)
    memo = models.TextField(blank=True)
    done = models.BooleanField()
    review = models.IntegerField(blank=True)
    motivation = models.IntegerField(blank=True)
    completiondate = models.DateField(blank=True)
    class Meta:
        db_table ="stressrelief"

# Create your models here.
