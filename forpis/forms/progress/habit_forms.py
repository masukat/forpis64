# -*- coding: utf-8 -*
from django import forms
from ...models.progress.habit_models import Habit,Habit_motivation,Habit_frequency,Habit_division

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['motivation','frequency','division','number','genre1','habit','memo','done1','done2','done3','done4','review','completiondate']

class HabitForm_motivation(forms.ModelForm):
    class Meta:
        model = Habit_motivation
        fields = ['motivation']

class HabitForm_frequency(forms.ModelForm):
    class Meta:
        model = Habit_frequency
        fields = ['frequency']

class HabitForm_division(forms.ModelForm):
    class Meta:
        model = Habit_division
        fields = ['division']
