from .models import ClientSell
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class TaskForm(ModelForm):
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
                'placeholder': 'Введите passportCode'
            }),
            "passportNumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите passportNumber'
            }),
        }