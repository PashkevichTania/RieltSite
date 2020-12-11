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
from .forms import SellForm, BuyForm, PropForm, FindAddress, FindRooms, FindArea, FindPrice


def index(request):
    employees = Employees.objects.all()
    return render(request, 'main/index.html', {
        'employees': employees,
    })


def property(request):
    property = Property.objects.filter(ifSelled=False)

    return render(request, 'main/property.html', {
        'property': property,
    })


def user_forms(request):
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
    return render(request, 'main/user_forms.html', context)


def requests(request):
    submitbutton = request.POST.get("submit")

    price = None
    area = None
    address = None
    rooms = None
    property = ''

    form1 = FindAddress(request.POST or None)
    form2 = FindRooms(request.POST or None)
    form3 = FindArea(request.POST or None)
    form4 = FindPrice(request.POST or None)
    if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
        address = form1.cleaned_data.get("address")
        rooms = form2.cleaned_data.get("rooms")
        area = form3.cleaned_data.get("area")
        price = form4.cleaned_data.get("price")
        if area is None:
            area = 1
        if price is None:
            price = 9*10**10
        if rooms is not None and address is not None:
            property = Property.objects.filter(address__contains=address, rooms=rooms, ifSelled=False,
                                               area__gt=area, price__lt=price)
        elif rooms is not None:
            property = Property.objects.filter(rooms=rooms, ifSelled=False,
                                               area__gt=area, price__lt=price)
        elif address is not None:
            property = Property.objects.filter(address__contains=address, ifSelled=False,
                                               area__gt=area, price__lt=price)
        else:
            property = Property.objects.filter(ifSelled=False,
                                               area__gt=area, price__lt=price)

    context = {'form1': form1,
               'form2': form2,
               'form3': form3,
               'form4': form4,
               'submitbutton': submitbutton,
               'property': property,
               'address': address,
               'rooms': rooms,
               'area': area,
               'price': price,
               }

    return render(request, 'main/requests.html', context)


def stuff_auth(request):
    return render(request, 'main/stuff_auth.html',)


def test(request):
    #property = Property.objects.filter(ifSelled=False)
    submitbutton = request.POST.get("submit")

    address = ''
    property = ''

    form = FindAddress(request.POST or None)
    if form.is_valid():
        address = form.cleaned_data.get("address")
        property = Property.objects.filter(address__contains=address)

    context = {'form': form,
               'address': address,
               'submitbutton': submitbutton,
               'property': property,
               }

    return render(request, 'main/test.html', context)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer



