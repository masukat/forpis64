# -*- coding: utf-8 -*
from django import forms
from ...models.progress.wannado_models import WannaDo,WannaDo_motivation,WannaDo_genre1,WannaDo_genre2,WannaDo_deadline

class WannaDoForm(forms.ModelForm):
    class Meta:
        model = WannaDo
        fields = ['done','motivation','review','genre1','genre2','plan','plandate','urllink','tag1','tag2','tag3','travelhour','travelmin','completiondate','deadline']

class WannaDoForm_motivation(forms.ModelForm):
   class Meta:
       model = WannaDo_motivation
       fields = ['motivation']

class WannaDoForm_genre1(forms.ModelForm):
   class Meta:
       model = WannaDo_genre1
       fields = ['genre1']

class WannaDoForm_genre2(forms.ModelForm):
   class Meta:
       model = WannaDo_genre2
       fields = ['genre2']

class WannaDoForm_deadline(forms.ModelForm):
   class Meta:
       model = WannaDo_deadline
       fields = ['deadline']
