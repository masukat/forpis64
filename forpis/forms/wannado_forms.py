# -*- coding: utf-8 -*
from django import forms
from ..models.wannado_models import WannaDo,WannaDo_motivation,WannaDo_genre1

class WannaDoForm(forms.ModelForm):
    class Meta:
        model = WannaDo
        fields = ['done','motivation','review','genre1','genre2','plan','urllink','tag1','tag2','tag3','travelhour','travelmin','completiondate']

class WannaDoForm_motivation(forms.ModelForm):
   class Meta:
       model = WannaDo_motivation
       fields = ['motivation']

class WannaDoForm_genre1(forms.ModelForm):
   class Meta:
       model = WannaDo_genre1
       fields = ['genre1']
