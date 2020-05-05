# -*- coding: utf-8 -*
from django import forms
from ...models.progress.stressrelief_models import ProgressStressrelief,ProgressStressrelief_motivation

class ProgressStressreliefForm(forms.ModelForm):
    class Meta:
        model = ProgressStressrelief
        fields = ['done','motivation','review','genre1','genre2','plan','urllink','memo','completiondate']

class ProgressStressreliefForm_motivation(forms.ModelForm):
    class Meta:
        model = ProgressStressrelief_motivation
        fields = ['motivation']
