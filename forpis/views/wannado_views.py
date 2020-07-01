from django.shortcuts import render
from django.shortcuts import redirect
from ..models.progress.wannado_models import WannaDo
from ..forms.progress.wannado_forms import WannaDoForm, WannaDoForm_motivation, WannaDoForm_genre1, WannaDoForm_genre2, WannaDoForm_deadline


def wannado(request):
    data_undone = WannaDo.objects.all().order_by('genre1', 'deadline')
    # 目標タブ
    data_undone_goal = WannaDo.objects.all().order_by('plandate')
    # 分野ごとのリスト
    data_genre1 = WannaDo.objects.all().order_by('deadline', 'motivation', 'genre2')
    # 完了リスト
    data_done = WannaDo.objects.all().order_by('completiondate').reverse()

    params = {
        'data_undone': data_undone,
        'data_undone_goal': data_undone_goal,
        'data_genre1': data_genre1,
        'data_done': data_done,
        'form': WannaDoForm(),
        'form_motivation': WannaDoForm_motivation(),
        'form_genre1': WannaDoForm_genre1(),
        'form_genre2': WannaDoForm_genre2(),
        'form_deadline': WannaDoForm_deadline(),
        'id': 0,
        'delete_flag': 0,
        }
    if (request.method == 'POST'):
        obj = WannaDo()
        wannado = WannaDoForm(request.POST, instance=obj)
        wannado_motivation = WannaDoForm_motivation(request.POST, instance=obj)
        wannado_genre1 = WannaDoForm_genre1(request.POST, instance=obj)
        wannado_genre2 = WannaDoForm_genre2(request.POST, instance=obj)
        wannado_deadline = WannaDoForm_deadline(request.POST, instance=obj)
        wannado.save()
        wannado_motivation.save()
        wannado_genre1.save()
        wannado_genre2.save()
        wannado_deadline.save()
        return redirect(to='/forpis/progress/wannado')
    return render(request, 'forpis/progress/wannado.html', params)


def wannado_edit(request, num):
    data_undone = WannaDo.objects.all().order_by('genre1', 'deadline')
    data_undone_goal = WannaDo.objects.all().order_by('plandate')
    data_genre1 = WannaDo.objects.all().order_by('deadline', 'motivation', 'genre2')
    data_done = WannaDo.objects.all().order_by('completiondate').reverse()

    obj = WannaDo.objects.get(id=num)

    # 分野、空白削除、max_length=100
    if obj.genre1 != '                                                                                                    ':
        obj.genre1 = obj.genre1.rstrip()
    # 項目、空白削除、max_length=100
    if obj.genre2 != '                                                                                                    ':
        obj.genre2 = obj.genre2.rstrip()
    # やりたいこと、空白削除、max_length=500
    if obj.plan != '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ':
        obj.plan = obj.plan.rstrip()
    # urllink、空白削除、max_length=2000
    if obj.urllink != '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ':
        obj.urllink = obj.urllink.rstrip()
    else:
        obj.urllink = ''
    # メモ、空白削除、max_length=100
    if obj.tag1 != '                                                                                                    ':
        obj.tag1 = obj.tag1.rstrip()
    else:
        obj.tag1 = ''

    if (request.method == 'POST'):
        wannado = WannaDoForm(request.POST, instance=obj)
        wannado_motivation = WannaDoForm_motivation(request.POST, instance=obj)
        wannado_genre1 = WannaDoForm_genre1(request.POST, instance=obj)
        wannado_genre2 = WannaDoForm_genre2(request.POST, instance=obj)
        wannado_deadline = WannaDoForm_deadline(request.POST, instance=obj)
        wannado.save()
        wannado_motivation.save()
        wannado_genre1.save()
        wannado_genre2.save()
        wannado_deadline.save()
        return redirect(to='/forpis/progress/wannado')
    params = {
        'data_undone': data_undone,
        'data_undone_goal': data_undone_goal,
        'data_genre1': data_genre1,
        'data_done': data_done,
        'form': WannaDoForm(instance=obj),
        'form_motivation': WannaDoForm_motivation(instance=obj),
        'form_genre1': WannaDoForm_genre1(instance=obj),
        'form_genre2': WannaDoForm_genre2(instance=obj),
        'form_deadline': WannaDoForm_deadline(instance=obj),
        'id': num,
        'delete_flag': 0,
        }
    return render(request, 'forpis/progress/wannado.html', params)


def wannado_delete(request, num):
    data_undone = WannaDo.objects.all().order_by('genre1', 'deadline')
    data_undone_goal = WannaDo.objects.all().order_by('plandate')
    data_genre1 = WannaDo.objects.all().order_by('deadline', 'motivation', 'genre2')
    data_done = WannaDo.objects.all().order_by('completiondate').reverse()

    wannado = WannaDo.objects.get(id=num)
    if (request.method == 'POST'):
        wannado.delete()
        return redirect(to='/forpis/progress/wannado')
    params = {
        'data_undone': data_undone,
        'data_undone_goal': data_undone_goal,
        'data_genre1': data_genre1,
        'data_done': data_done,
        'obj': wannado,
        'id': num,
        'delete_flag': 1,
        }
    return render(request, 'forpis/progress/wannado.html', params)
# Create your views here.
