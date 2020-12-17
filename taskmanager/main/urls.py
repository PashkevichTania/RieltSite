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
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('tables', views.tables, name='tables'),
    path('staff_deals', views.staff_deals, name='staff_deals'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('backup/<str:pk>', views.backup, name='backup'),
    path('update/<str:pk>', views.MyUpdateView.as_view(), name='update'),
    # path('test', views.test, name='test'),
]

urlpatterns += router.urls