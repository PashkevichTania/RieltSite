from django.shortcuts import render, redirect
from .models import Employees
from .models import ClientBuy
from .models import ClientSell
from .models import Property
from .models import SelledProperty
from rest_framework import viewsets
from .serializers import EmployeesSerializer
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import SellForm, BuyForm, PropForm


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
    error1 = ''
    error2 = ''
    error3 = ''
    if request.method == 'POST':
        form1 = BuyForm(request.POST)
        form2 = SellForm(request.POST)
        form3 = PropForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
        else:
            error1 = 'Форма была неверной'
        if form2.is_valid():
            form2.save()
            return redirect('home')
        else:
            error2 = 'Форма была неверной'
        if form3.is_valid():
            form3.save()
            return redirect('home')
        else:
            error3 = 'Форма была неверной'
    form1 = BuyForm()
    form2 = SellForm()
    form3 = PropForm()
    context = {
        'form1': form1,
        'error1': error1,
        'form2': form2,
        'error2': error2,
        'form3': form3,
        'error3': error3,
    }
    return render(request, 'main/requests.html', context)


def stuff_auth(request):
    return render(request, 'main/stuff_auth.html',)


def test(request):
    return render(request, 'main/test.html',)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer



