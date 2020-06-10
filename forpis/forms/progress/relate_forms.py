# -*- coding: utf-8 -*
from django import forms
from ...models.progress.relate_models import Relate,Relate_motivation

class RelateForm(forms.ModelForm):
    class Meta:
        model = Relate
        fields = ['name','thanksgenre1','thanks','thanksdate','thanksurllink','thanksmemo','thanksreview','plangenre1','plan','plandate','planurllink','planmemo','done','planreview','motivation','completiondate']

class RelateForm_motivation(forms.ModelForm):
    class Meta:
        model = Relate_motivation
        fields = ['motivation']
