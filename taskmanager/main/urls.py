from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tables', views.tables, name='tables'),
    path('sql', views.sql, name='sql'),
]
