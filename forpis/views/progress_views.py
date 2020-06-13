from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ..models.progress.habit_models import Habit
from ..forms.progress.habit_forms import HabitForm,HabitForm_motivation,HabitForm_frequency,HabitForm_division,HabitForm_habitgenre1,HabitForm_probgenre1,HabitForm_probgenre2
from ..models.progress.relief_models import Relief
from ..forms.progress.relief_forms import ReliefForm,ReliefForm_motivation
from ..models.progress.relate_models import Relate
from ..forms.progress.relate_forms import RelateForm,RelateForm_motivation

import requests
from bs4 import BeautifulSoup


def progress_relate(request):
    data_done_thanks = Relate.objects.all().order_by('name','thanksdate').reverse()
    data_undone_plan = Relate.objects.all().order_by('motivation','plangenre1','plan').reverse()
    data_done_plan = Relate.objects.all().order_by('completiondate','review').reverse()

    params = {
        'data_done_thanks':data_done_thanks,
        'data_undone_plan':data_undone_plan,
        'data_done_plan':data_done_plan,
        'form':RelateForm(),
        'form_motivation':RelateForm_motivation(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = Relate()
        relate = RelateForm(request.POST, instance=obj)
        motivation = RelateForm_motivation(request.POST, instance=obj)
        relate.save()
        motivation.save()
        return redirect(to='/forpis/progress/relate')
    return render(request, 'forpis/progress/relate.html', params)

def progress_relate_edit(request,num):
    data_done_thanks = Relate.objects.all().order_by('thanksreview').reverse()
    data_undone_plan = Relate.objects.all().order_by('motivation','plangenre1','plan').reverse()
    data_done_plan = Relate.objects.all().order_by('completiondate','review').reverse()

    obj = Relate.objects.get(id=num)

    if (request.method == 'POST'):
        relate = RelateForm(request.POST, instance=obj)
        motivation = RelateForm_motivation(request.POST, instance=obj)
        relate.save()
        motivation.save()
        return redirect(to='/forpis/progress/relate')
    params = {
        'data_done_thanks':data_done_thanks,
        'data_undone_plan':data_undone_plan,
        'data_done_plan':data_done_plan,
        'form':RelateForm(instance=obj),
        'form_motivation':RelateForm_motivation(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/relate.html', params)

def progress_relate_delete(request,num):
    data_done_thanks = Relate.objects.all().order_by('thanksreview').reverse()
    data_undone_plan = Relate.objects.all().order_by('motivation','plangenre1','plan').reverse()
    data_done_plan = Relate.objects.all().order_by('completiondate','review').reverse()

    relate = Relate.objects.get(id=num)
    if (request.method == 'POST'):
        relate.delete()
        return redirect(to='/forpis/progress/relate')
    params = {
        'data_done_thanks':data_done_thanks,
        'data_undone_plan':data_undone_plan,
        'data_done_plan':data_done_plan,
        'obj':relate,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/relate.html', params)






def progress_habit(request):
    data_problem = Habit.objects.all().order_by('probgenre1','probgenre2' ,'updated_at').reverse()
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','habitgenre1').reverse()

    params = {
        'data_problem':data_problem,
        'data_habit':data_habit,
        'form':HabitForm(),
        'form_motivation':HabitForm_motivation(),
        'form_frequency':HabitForm_frequency(),
        'form_division':HabitForm_division(),
        'form_habitgenre1':HabitForm_habitgenre1(),
        'form_probgenre1':HabitForm_probgenre1(),
        'form_probgenre2':HabitForm_probgenre2(),
        'id':0,
        'delete_flag':0,
        }
    if (request.method == 'POST'):
        obj = Habit()
        habit = HabitForm(request.POST, instance=obj)
        motivation = HabitForm_motivation(request.POST, instance=obj)
        frequency = HabitForm_frequency(request.POST, instance=obj)
        division = HabitForm_division(request.POST, instance=obj)
        habitgenre1 = HabitForm_habitgenre1(request.POST, instance=obj)
        probgenre1 = HabitForm_probgenre1(request.POST, instance=obj)
        probgenre2 = HabitForm_probgenre2(request.POST, instance=obj)
        habit.save()
        motivation.save()
        frequency.save()
        division.save()
        habitgenre1.save()
        probgenre1.save()
        probgenre2.save()
        return redirect(to='/forpis/progress/habit')
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_edit(request,num):
    data_problem = Habit.objects.all().order_by('probgenre1','probgenre2' ,'updated_at').reverse()
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','habitgenre1').reverse()

    obj = Habit.objects.get(id=num)

    if (request.method == 'POST'):
        habit = HabitForm(request.POST, instance=obj)
        motivation = HabitForm_motivation(request.POST, instance=obj)
        frequency = HabitForm_frequency(request.POST, instance=obj)
        division = HabitForm_division(request.POST, instance=obj)
        habitgenre1 = HabitForm_habitgenre1(request.POST, instance=obj)
        probgenre1 = HabitForm_probgenre1(request.POST, instance=obj)
        probgenre2 = HabitForm_probgenre2(request.POST, instance=obj)
        habit.save()
        motivation.save()
        frequency.save()
        division.save()
        habitgenre1.save()
        probgenre1.save()
        probgenre2.save()
        return redirect(to='/forpis/progress/habit')
    params = {
        'data_problem':data_problem,
        'data_habit':data_habit,
        'form':HabitForm(instance=obj),
        'form_motivation':HabitForm_motivation(instance=obj),
        'form_frequency':HabitForm_frequency(instance=obj),
        'form_division':HabitForm_division(instance=obj),
        'form_habitgenre1':HabitForm_habitgenre1(instance=obj),
        'form_probgenre1':HabitForm_probgenre1(instance=obj),
        'form_probgenre2':HabitForm_probgenre2(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/habit.html', params)

def progress_habit_delete(request,num):
    data_problem = Habit.objects.all().order_by('probgenre1','probgenre2' ,'updated_at').reverse()
    data_habit = Habit.objects.all().order_by('motivation','frequency','division','habitgenre1').reverse()

    habit = Habit.objects.get(id=num)
    if (request.method == 'POST'):
        habit.delete()
        return redirect(to='/forpis/progress/habit')
    params = {
        'data_problem':data_problem,
        'data_habit':data_habit,
        'obj':habit,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/habit.html', params)


def progress_summary(request):
    return render(request, 'forpis/progress/summary.html')








def progress_relief(request):
    data_undone = Relief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = Relief.objects.all().order_by('completiondate','review').reverse()
    titles = search_movieTitles()
    titlesNum = len(titles)
    highlights = search_movieHighlights()

    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'titles':titles,
        'range':range(titlesNum),
        'highlights':highlights,
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
    titles = search_movieTitles()
    titlesNum = len(titles)
    highlights = search_movieHighlights()

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
        'titles':titles,
        'range':range(titlesNum),
        'highlights':highlights,
        'form':ReliefForm(instance=obj),
        'form_motivation':ReliefForm_motivation(instance=obj),
        'id':num,
        'delete_flag':0,
        }
    return render(request, 'forpis/progress/relief.html', params)

def progress_relief_delete(request,num):
    data_undone = Relief.objects.all().order_by('motivation','genre1','genre2','plan').reverse()
    data_done = Relief.objects.all().order_by('completiondate','review').reverse()
    titles = search_movieTitles()
    titlesNum = len(titles)
    highlights = search_movieHighlights()

    relief = Relief.objects.get(id=num)
    if (request.method == 'POST'):
        relief.delete()
        return redirect(to='/forpis/progress/relief')
    params = {
        'data_undone':data_undone,
        'data_done':data_done,
        'titles':titles,
        'range':range(titlesNum),
        'highlights':highlights,
        'obj':relief,
        'id':num,
        'delete_flag':1,
        }
    return render(request, 'forpis/progress/relief.html', params)

def search_movieTitles():
    # WebサイトのURLを指定
    url = "https://vokka.jp/16136"
    # Requestsを利用してWebページを取得する
    r = requests.get(url)
    # BeautifulSoupを利用してWebページを解析する
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup.find_allを利用して、見出しのタイトルを取得する
    titlesAll = soup.find_all("h2", class_="c-post-title--title")
    titles = []

    for t in titlesAll:
        if '【' in t.getText():
            titles.append(t.getText())
    return titles

def search_movieHighlights():
    # WebサイトのURLを指定
    url = "https://vokka.jp/16136"
    # Requestsを利用してWebページを取得する
    r = requests.get(url)
    # BeautifulSoupを利用してWebページを解析する
    soup = BeautifulSoup(r.text, 'html.parser')
    # soup.find_allを利用して、見出しのタイトルを取得する
    text = soup.find_all("p", class_="c-post-txt")
    HighlightsAll = []
    Highlights = []
    d = '・・・'

    for t in text:
        HighlightsAll.append(t.getText())
    for i in range(1,27,2):
        if len(HighlightsAll[i]) < 300:
            Highlights.append(HighlightsAll[i][0:301])
        else:
            Highlights.append(HighlightsAll[i][0:301] + d)
    return Highlights




def progress_earnmoney(request):
    return render(request, 'forpis/progress/earn.html')
