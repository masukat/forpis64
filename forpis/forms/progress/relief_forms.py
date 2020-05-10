# -*- coding: utf-8 -*
from django import forms
from ...models.progress.relief_models import Relief,Relief_motivation

class ReliefForm(forms.ModelForm):
    class Meta:
        model = Relief
        fields = ['done','motivation','review','genre1','genre2','plan','urllink','memo','completiondate']

class ReliefForm_motivation(forms.ModelForm):
    class Meta:
        model = Relief_motivation
        fields = ['motivation']
