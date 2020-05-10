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
    path('progress/relief', progress_views.progress_relief, name='progress_relief'),
    path('progress/relief/edit/<int:num>', progress_views.progress_relief_edit, name='progress_relief_edit'),
    path('progress/relief/delete/<int:num>', progress_views.progress_relief_delete, name='progress_relief_delete'),
    path('progress/earn', progress_views.progress_earnmoney, name='progress_earn'),
    path('progress/relate', progress_views.progress_relationship, name='progress_relate'),
]
