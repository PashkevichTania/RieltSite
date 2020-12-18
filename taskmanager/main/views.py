from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Employees, ClientBuy, ClientSell, Property, SelledProperty, DealsBackup
from rest_framework import viewsets
from .serializers import EmployeesSerializer
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import SellForm, BuyForm, PropForm, FindAddress, FindRooms, FindArea, FindPrice, AuthUserForm, SelledPropForm
from django.contrib.messages.views import SuccessMessageMixin


# главная страница
def index(request):
    return render(request, 'main/index.html',)


# недвижимость
def property(request):
    property = Property.objects.filter(ifSelled=False)
    return render(request, 'main/property.html', {
        'property': property,
    })


# для продавцов\покупателей
def user_forms(request):
    error_buy = ''
    error_sell = ''
    error_prop = ''
    if request.method == 'POST':
        form_buy = BuyForm(request.POST)
        form_sell = SellForm(request.POST)
        form_prop = PropForm(request.POST)
        if form_buy.is_valid():
            form_buy.save()
            messages.success(request, "Успешно")
        else:
            error_buy = 'Форма была неверной'
        if form_sell.is_valid():
            form_sell.save()
            messages.success(request, "Успешно")
        else:
            error_sell = 'Форма была неверной'
        if form_prop.is_valid():
            form_prop.save()
            messages.success(request, "Недвижимость добавлена")
        else:
            error_prop = 'Форма была неверной'
    form_buy = BuyForm()
    form_sell = SellForm()
    form_prop = PropForm()
    context = {
        'form_buy': form_buy,
        'error_buy': error_buy,
        'form_sell': form_sell,
        'error_sell': error_sell,
        'form_prop': form_prop,
        'error_prop': error_prop,
    }
    return render(request, 'main/user_forms.html', context)


# поиск квартир
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
            property = Property.objects.filter(ifSelled=False)

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


# serializer for API
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class MyprojectLoginView(LoginView):
    template_name = 'staff/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('tables')


    def get_success_url(self):
        return self.success_url


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')


# таблицы
def tables(request):
    property = Property.objects.all()
    client_sell = ClientSell.objects.all()
    client_buy = ClientBuy.objects.all()
    selled_prop = SelledProperty.objects.prefetch_related('applicationCode__seller__property_set')

    return render(request, 'staff/tables.html', {
        'property': property,
        'client_sell': client_sell,
        'client_buy': client_buy,
        'selled_prop': selled_prop,
    })


# сделки
def staff_deals(request):
    selled_prop = SelledProperty.objects.all()
    error = ''
    if request.method == 'POST':
        form = SelledPropForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Сделка добавлена")
        else:
            error = 'Форма была неверной'

    form = SelledPropForm()
    context = {
        'form': form,
        'error': error,
        'selled_prop': selled_prop,
    }

    return render(request, 'staff/staff_deals.html', context)


# для кнопки удалить
def delete(request, pk):
    get_selled_prop = SelledProperty.objects.get(pk=pk)
    get_selled_prop.delete()

    return redirect(reverse('staff_deals'))


# для кнопки обновить
class MyUpdateView(SuccessMessageMixin, UpdateView):
    model = SelledProperty
    template_name = 'staff/staff_deals.html'
    form_class = SelledPropForm
    success_url = reverse_lazy('staff_deals')
    success_message = 'Запись успешно обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs


# для кнопки резервного копирования
def backup(request, pk):
    backupqs = SelledProperty.objects.prefetch_related('applicationCode__seller__property_set').get(pk=pk)
    b = DealsBackup(contractCode = backupqs.contractCode,
                    applicationCode = backupqs.applicationCode,
                    dateOfOrder=backupqs.applicationCode.dateOfOrder,
                    dateOfOperation=backupqs.dateOfOperation,
                    employee=backupqs.employee,
                    buyer=backupqs.buyer,
                    seller=backupqs.applicationCode.seller,
                    price=backupqs.applicationCode.price,
                    profit=backupqs.profit,
                    )
    b.save()
    return redirect(reverse('staff_deals'))





