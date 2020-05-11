from django.db import models

MOTIVATION_CHOISES=(
    ('5','5'),
    ('4','4'),
    ('3','3'),
    ('2','2'),
    ('1','1'),
)

GENRE1_CHOISES=(
    ('勉強','勉強'),
    ('本','本'),
    ('趣味','趣味'),
    ('コロナ後','コロナ後'),
    ('他','他'),
)

GENRE2_CHOISES=(
    ('目標','目標'),
    ('お金','お金'),
    ('IT','IT'),
    ('資格','資格'),
    ('動画','動画'),
    ('語学','語学'),
    ('時事','時事'),
    ('考え整理','考え整理'),
    ('啓発','啓発'),
    ('マンガ','マンガ'),
    ('動画','動画'),
    ('youtube','youtube'),
    ('netflix','netflix'),
    ('欲しい','欲しい'),
    ('美容','美容'),
    ('他','他'),
)

class WannaDo_motivation(models.Model):
    motivation = models.IntegerField(blank=True,choices=MOTIVATION_CHOISES)

class WannaDo_genre1(models.Model):
    genre1 = models.CharField(max_length=100,choices=GENRE1_CHOISES)

class WannaDo_genre2(models.Model):
    genre2 = models.CharField(max_length=100,blank=True,choices=GENRE2_CHOISES)

class WannaDo(models.Model):
    genre1 = models.CharField(max_length=100)
    genre2 = models.CharField(max_length=100,blank=True)
    plan = models.CharField(max_length=500)
    urllink = models.CharField(max_length=2000,blank=True)
    tag1 = models.CharField(max_length=100,blank=True)
    tag2 = models.CharField(max_length=100,blank=True)
    tag3 = models.CharField(max_length=100,blank=True)
    done = models.BooleanField()
    review = models.IntegerField(blank=True)
    motivation = models.IntegerField(blank=True)
    travelhour = models.IntegerField(blank=True)
    travelmin = models.IntegerField(blank=True)
    completiondate = models.DateField(blank=True)
    class Meta:
        db_table ="wannado"



# Create your models here.
