from .models import ClientSell, ClientBuy, Property
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ModelChoiceField, DateInput, Select


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