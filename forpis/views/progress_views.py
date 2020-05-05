from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ..models.progress.habit_models import ProgressHabit
from ..forms.progress.habit_forms import ProgressHabitForm,ProgressHabitForm_motivation,ProgressHabitForm_frequency,ProgressHabitForm_division
from ..models.progress.stressrelief_models import ProgressStressrelief
from ..forms.progress.stressrelief_forms import ProgressStressreliefForm,ProgressStressreliefForm_motivation

def progress_summary(request):
    return render(request, 'forpis/progress/summary.html')

def progress_habit(request):
    data_habit = ProgressHabit.objects.all().order_by('motivation','frequency').reverse()
    data_undone = ProgressHabit.objects.all().order_by('motivation','genre1').reverse()
    data_done = ProgressHabit.objects.all().order_by('completiondate','review').reverse()

    params = {
        'data_habit':data_habit,
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ProgressHabitForm(),
        'form_motivation':ProgressHabitForm_motivation(),
        'form_frequency':ProgressHabitForm_frequency(),
        'form_division':ProgressHabitForm_division(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = ProgressHabit()
        habit = ProgressHabitForm(request.POST, instance=obj)
        habit_motivation = ProgressHabitForm_motivation(request.POST, instance=obj)
        habit_frequency = ProgressHabitForm_frequency(request.POST, instance=obj)
        habit_division = ProgressHabitForm_division(request.POST, instance=obj)
        habit.save()
        habit_motivation.save()
        habit_frequency.save()
        habit_division.save()
        return redirect(to='/forpis/progress/habit')
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_edit(request,num):
    data_habit = ProgressHabit.objects.all().order_by('motivation','frequency').reverse()
    data_undone = ProgressHabit.objects.all().order_by('motivation','genre1').reverse()
    data_done = ProgressHabit.objects.all().order_by('completiondate','review').reverse()

    obj = ProgressHabit.objects.get(id=num)

    if (request.method == 'POST'):
        habit = ProgressHabitForm(request.POST, instance=obj)
        habit_motivation = ProgressHabitForm_motivation(request.POST, instance=obj)
        habit_frequency = ProgressHabitForm_frequency(request.POST, instance=obj)
        habit_division = ProgressHabitForm_division(request.POST, instance=obj)
        habit.save()
        habit_motivation.save()
        habit_frequency.save()
        habit_division.save()
        return redirect(to='/forpis/progress/habit')
    params = {
        'data_habit':data_habit,
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ProgressHabitForm(instance=obj),
        'form_motivation':ProgressHabitForm_motivation(instance=obj),
        'form_frequency':ProgressHabitForm_frequency(instance=obj),
        'form_division':ProgressHabitForm_division(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_delete(request,num):
    data_habit = ProgressHabit.objects.all().order_by('motivation','frequency').reverse()
    data_undone = ProgressHabit.objects.all().order_by('motivation','genre1').reverse()
    data_done = ProgressHabit.objects.all().order_by('completiondate','review').reverse()

    habit = ProgressHabit.objects.get(id=num)
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






def progress_stressrelief(request):
    data_undone = ProgressStressrelief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = ProgressStressrelief.objects.all().order_by('completiondate','review').reverse()

    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ProgressStressreliefForm(),
        'form_motivation':ProgressStressreliefForm_motivation(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = ProgressStressrelief()
        stressrelief = ProgressStressreliefForm(request.POST, instance=obj)
        stressrelief_motivation = ProgressStressreliefForm_motivation(request.POST, instance=obj)
        stressrelief.save()
        stressrelief_motivation.save()
        return redirect(to='/forpis/progress/stressrelief')
    return render(request, 'forpis/progress/stressrelief.html', params)

def progress_stressrelief_edit(request,num):
    data_undone = ProgressStressrelief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = ProgressStressrelief.objects.all().order_by('completiondate','review').reverse()

    obj = ProgressStressrelief.objects.get(id=num)

    if (request.method == 'POST'):
        stressrelief = ProgressStressreliefForm(request.POST, instance=obj)
        stressrelief_motivation = ProgressStressreliefForm_motivation(request.POST, instance=obj)
        stressrelief.save()
        stressrelief_motivation.save()
        return redirect(to='/forpis/progress/stressrelief')
    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'form':ProgressStressreliefForm(instance=obj),
        'form_motivation':ProgressStressreliefForm_motivation(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/stressrelief.html', params)

def progress_stressrelief_delete(request,num):
    data_undone = ProgressStressrelief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = ProgressStressrelief.objects.all().order_by('completiondate','review').reverse()

    stressrelief = ProgressStressrelief.objects.get(id=num)
    if (request.method == 'POST'):
        stressrelief.delete()
        return redirect(to='/forpis/progress/stressrelief')
    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'obj':stressrelief,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/stressrelief.html', params)

def progress_earnmoney(request):
    return render(request, 'forpis/progress/earnmoney.html')

def progress_relationship(request):
    return render(request, 'forpis/progress/relationship.html')
