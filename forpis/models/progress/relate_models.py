from django.db import models


MOTIVATION_CHOISES = (
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


class Relate_motivation(models.Model):
    motivation = models.IntegerField(blank=True, default=4, choices=MOTIVATION_CHOISES)


class Relate(models.Model):
    name = models.CharField(max_length=100)
    thanksgenre1 = models.CharField(max_length=100, blank=True)
    thanks = models.TextField(blank=True)
    thanksdate = models.DateField(blank=True)
    thanksurllink = models.TextField(blank=True)
    thanksmemo = models.TextField(blank=True)
    thanksreview = models.IntegerField(blank=True)

    plangenre1 = models.CharField(max_length=100, blank=True)
    plan = models.TextField(blank=True)
    plandate = models.DateField(blank=True)
    planurllink = models.TextField(blank=True)
    planmemo = models.TextField(blank=True)
    done = models.BooleanField()
    planreview = models.IntegerField(blank=True)
    motivation = models.IntegerField(blank=True)
    completiondate = models.DateField(blank=True)

    class Meta:
        db_table = "relate"
