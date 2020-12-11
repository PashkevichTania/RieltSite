from django.urls import path
from rest_framework import routers
from . import views
from .views import EmployeesViewSet


router = routers.SimpleRouter()
router.register('api/employees', EmployeesViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('property', views.property, name='property'),
    path('requests', views.requests, name='requests'),
    path('user_forms', views.user_forms, name='user_forms'),
    path('stuff_auth', views.stuff_auth, name='stuff_auth'),
    path('test', views.test, name='test'),
]

urlpatterns += router.urls