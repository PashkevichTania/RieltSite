from .models import ClientSell, ClientBuy, Property
from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField, DateInput, Select
from django import forms


class SellForm(ModelForm):
    class Meta:
        model = ClientSell
        fields = ["FIO",
                  "address",
                  "tel",
                  "passportCode",
                  "passportNumber"]
        widgets = {
            "FIO": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "tel": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите tel'
            }),
            "passportCode": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите код паспорта'
            }),
            "passportNumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите индентификационный номер'
            }),
        }


class BuyForm(ModelForm):
    class Meta:
        model = ClientBuy
        fields = ["FIO",
                  "address",
                  "tel",
                  "passportCode",
                  "passportNumber"]
        widgets = {
            "FIO": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "tel": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "passportCode": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите код паспорта'
            }),
            "passportNumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите индентификационный номер',
            }),
        }


class PropForm(ModelForm):
    class Meta:
        model = Property
        fields = ["dateOfOrder",
                  "name",
                  "area",
                  "rooms",
                  "address",
                  "price",
                  "seller"]
        widgets = {
            "dateOfOrder": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату составления заказа (dd.mm.yyyy)'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }),
            "area": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите площадь'
            }),
            "rooms": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество комнат'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "seller": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберете продавца',
            }),
        }


class FindAddress(forms.Form):
    address = forms.CharField(label='Адрес содержит', max_length=50, required=False)


class FindRooms(forms.Form):
    rooms = forms.IntegerField(label='Количество комнат', required=False)


class FindArea(forms.Form):
    area = forms.IntegerField(label='Минимальная площадь', required=False)


class FindPrice(forms.Form):
    price = forms.IntegerField(label='Максимальная цена', required=False)
