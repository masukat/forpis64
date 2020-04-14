from django.urls import path
from . import views

urlpatterns = [
    path('wannado', views.wannado, name='wannado'),
    path('wannado/edit/<int:num>', views.wannado_edit, name='wannado_edit'),
    path('wannado/delete/<int:num>', views.wannado_delete, name='wannado_delete'),
]
