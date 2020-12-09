from django.shortcuts import render, redirect
from .models import Employees
from .models import ClientBuy
from .models import ClientSell
from .models import Property
from .models import SelledProperty
import pyodbc
from rest_framework import viewsets
from .serializers import EmployeesSerializer
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import TaskForm


def index(request):
    employees = Employees.objects.all()
    return render(request, 'main/index.html', {
        'employees': employees,
    })


def tables(request):
    employees = Employees.objects.all()
    clientBuy = ClientBuy.objects.all()
    clientSell = ClientSell.objects.all()
    property = Property.objects.all()
    selledProperty = SelledProperty.objects.all()

    return render(request, 'main/tables.html', {
        'employees': employees,
        'clientBuy': clientBuy,
        'clientSell': clientSell,
        'property': property,
        'selledProperty': selledProperty
    })


def requests(request):
    employees = Employees.objects.all()
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/requests.html', context)


def stuff_auth(request):

    return render(request, 'main/stuff_auth.html',)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer



