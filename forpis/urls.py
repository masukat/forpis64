from django.urls import path
from .views import wannado_views
from .views import progress_views

urlpatterns = [
    path('wannado', wannado_views.wannado, name='wannado'),
    path('wannado/edit/<int:num>', wannado_views.wannado_edit, name='wannado_edit'),
    path('wannado/delete/<int:num>', wannado_views.wannado_delete, name='wannado_delete'),
    path('progress/summary', progress_views.progress_summary, name='progress_summary'),
    path('progress/habit', progress_views.progress_habit, name='progress_habit'),
    path('progress/habit/edit/<int:num>', progress_views.progress_habit_edit, name='progress_habit_edit'),
    path('progress/habit/delete/<int:num>', progress_views.progress_habit_delete, name='progress_habit_delete'),
    path('progress/stressrelief', progress_views.progress_stressrelief, name='progress_stressrelief'),
    path('progress/stressrelief/edit/<int:num>', progress_views.progress_stressrelief_edit, name='progress_stressrelief_edit'),
    path('progress/stressrelief/delete/<int:num>', progress_views.progress_stressrelief_delete, name='progress_stressrelief_delete'),
    path('progress/earnmoney', progress_views.progress_earnmoney, name='progress_earnmoney'),
    path('progress/relationship', progress_views.progress_relationship, name='progress_relationship'),
]
