from django.db import models

class WannaDo(models.Model):
    done = models.BooleanField()
    motivation = models.IntegerField(blank=True)
    review = models.IntegerField(blank=True)
    genre1 = models.CharField(max_length=100)
    genre2 = models.CharField(max_length=100,blank=True)
    plan = models.CharField(max_length=500)
    travelhour = models.IntegerField(blank=True)
    travelmin = models.IntegerField(blank=True)
    urllink = models.CharField(max_length=2000,blank=True)
    tag1 = models.CharField(max_length=100,blank=True)
    tag2 = models.CharField(max_length=100,blank=True)
    tag3 = models.CharField(max_length=100,blank=True)
    completiondate = models.DateField(blank=True)

    class Meta:
        db_table ="forpis_wannado"



# Create your models here.
