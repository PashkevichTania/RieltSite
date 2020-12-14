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
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('tables', views.tables, name='tables'),
    path('stuff_forms', views.stuff_forms, name='stuff_forms'),
]

urlpatterns += router.urls