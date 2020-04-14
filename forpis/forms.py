# -*- coding: utf-8 -*
from django import forms
from.models import WannaDo

class WannaDoForm(forms.ModelForm):
    class Meta:
        model = WannaDo
        fields = ['done','motivation','review','genre1','genre2','plan','urllink','tag1','tag2','tag3','travelhour','travelmin','completiondate']
