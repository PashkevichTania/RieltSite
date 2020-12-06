from django.shortcuts import render, redirect
from .models import Employees
from .models import ClientBuy
from .models import ClientSell
from .models import Property
from .models import SelledProperty
import pyodbc


def index(request):
    return render(request, 'main/index.html')


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
    return render(request, 'main/requests.html')

