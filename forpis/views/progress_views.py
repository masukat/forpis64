from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ..models.progress.habit_models import Habit
from ..forms.progress.habit_forms import HabitForm,HabitForm_motivation,HabitForm_frequency,HabitForm_division
from ..models.progress.relief_models import Relief
from ..forms.progress.relief_forms import ReliefForm,ReliefForm_motivation

def progress_summary(request):
    return render(request, 'forpis/progress/summary.html')

def progress_habit(request):
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','genre1').reverse()
    data_undone = Habit.objects.all().order_by('motivation','genre1').reverse()
    data_done = Habit.objects.all().order_by('completiondate','review').reverse()

    params = {
        'data_habit':data_habit,
        'data_undone':data_undone,
        'data_done':data_done,
        'form':HabitForm(),
        'form_motivation':HabitForm_motivation(),
        'form_frequency':HabitForm_frequency(),
        'form_division':HabitForm_division(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = Habit()
        habit = HabitForm(request.POST, instance=obj)
        habit_motivation = HabitForm_motivation(request.POST, instance=obj)
        habit_frequency = HabitForm_frequency(request.POST, instance=obj)
        habit_division = HabitForm_division(request.POST, instance=obj)
        habit.save()
        habit_motivation.save()
        habit_frequency.save()
        habit_division.save()
        return redirect(to='/forpis/progress/habit')
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_edit(request,num):
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','genre1').reverse()
    data_undone = Habit.objects.all().order_by('motivation','genre1').reverse()
    data_done = Habit.objects.all().order_by('completiondate','review').reverse()

    obj = Habit.objects.get(id=num)

    if (request.method == 'POST'):
        habit = HabitForm(request.POST, instance=obj)
        habit_motivation = HabitForm_motivation(request.POST, instance=obj)
        habit_frequency = HabitForm_frequency(request.POST, instance=obj)
        habit_division = HabitForm_division(request.POST, instance=obj)
        habit.save()
        habit_motivation.save()
        habit_frequency.save()
        habit_division.save()
        return redirect(to='/forpis/progress/habit')
    params = {
        'data_habit':data_habit,
        'data_undone':data_undone,
        'data_done':data_done,
        'form':HabitForm(instance=obj),
        'form_motivation':HabitForm_motivation(instance=obj),
        'form_frequency':HabitForm_frequency(instance=obj),
        'form_division':HabitForm_division(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_delete(request,num):
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','genre1').reverse()
    data_undone = Habit.objects.all().order_by('motivation','genre1').reverse()
    data_done = Habit.objects.all().order_by('completiondate','review').reverse()

    habit = Habit.objects.get(id=num)
    if (request.method == 'POST'):
        habit.delete()
        return redirect(to='/forpis/progress/habit')
    params = {
        'data_habit':data_habit,
        'data_undone':data_undone,
        'data_done':data_done,
        'obj':habit,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/habit.html', params)






def progress_relief(request):
    data_undone = Relief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = Relief.objects.all().order_by('completiondate','review').reverse()

    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ReliefForm(),
        'form_motivation':ReliefForm_motivation(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = Relief()
        relief = ReliefForm(request.POST, instance=obj)
        relief_motivation = ReliefForm_motivation(request.POST, instance=obj)
        relief.save()
        relief_motivation.save()
        return redirect(to='/forpis/progress/relief')
    return render(request, 'forpis/progress/relief.html', params)

def progress_relief_edit(request,num):
    data_undone = Relief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = Relief.objects.all().order_by('completiondate','review').reverse()

    obj = Relief.objects.get(id=num)

    if (request.method == 'POST'):
        relief = ReliefForm(request.POST, instance=obj)
        relief_motivation = ReliefForm_motivation(request.POST, instance=obj)
        relief.save()
        relief_motivation.save()
        return redirect(to='/forpis/progress/relief')
    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ReliefForm(instance=obj),
        'form_motivation':ReliefForm_motivation(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/relief.html', params)

def progress_relief_delete(request,num):
    data_undone = Relief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = Relief.objects.all().order_by('completiondate','review').reverse()

    relief = Relief.objects.get(id=num)
    if (request.method == 'POST'):
        relief.delete()
        return redirect(to='/forpis/progress/relief')
    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'obj':relief,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/relief.html', params)

def progress_earnmoney(request):
    return render(request, 'forpis/progress/earn.html')

def progress_relationship(request):
    return render(request, 'forpis/progress/relate.html')
