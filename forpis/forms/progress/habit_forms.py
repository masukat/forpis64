# -*- coding: utf-8 -*
from django import forms
from ...models.progress.habit_models import ProgressHabit,ProgressHabit_motivation,ProgressHabit_frequency,ProgressHabit_division

class ProgressHabitForm(forms.ModelForm):
    class Meta:
        model = ProgressHabit
        fields = ['motivation','frequency','division','number','genre1','habit','memo','done1','done2','done3','done4','review','completiondate']

class ProgressHabitForm_motivation(forms.ModelForm):
    class Meta:
        model = ProgressHabit_motivation
        fields = ['motivation']

class ProgressHabitForm_frequency(forms.ModelForm):
    class Meta:
        model = ProgressHabit_frequency
        fields = ['frequency']

class ProgressHabitForm_division(forms.ModelForm):
    class Meta:
        model = ProgressHabit_division
        fields = ['division']
