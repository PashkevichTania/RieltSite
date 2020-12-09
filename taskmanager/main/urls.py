from django.urls import path
from rest_framework import routers
from . import views
from .views import EmployeesViewSet

urlpatterns = [
    path('', views.index, name='home'),
    path('tables', views.tables, name='tables'),
    path('requests', views.requests, name='requests'),
    path('stuff_auth', views.stuff_auth, name='stuff_auth'),
]

# Создаем router и регистрируем наш ViewSet
#router = routers.DefaultRouter()
#router.register(r'Employees', EmployeesViewSet)


# URLs настраиваются автоматически роутером
#urlpatterns = router.urls