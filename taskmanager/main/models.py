from django.db import models
import uuid


class Employees(models.Model):
    employeeCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True, )
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    post = models.CharField(verbose_name='Должность', max_length=50)
    dateOfEmployment = models.DateField(verbose_name='Дата найма')
    address = models.CharField(verbose_name='Адресс', max_length=50)
    tel = models.IntegerField(verbose_name='Телефон')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class ClientBuy(models.Model):
    buyerCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True)
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    address = models.CharField(verbose_name='Адресс', max_length=50)
    tel = models.IntegerField(verbose_name='Телефон')
    passportCode = models.CharField(verbose_name='Код поспорта', help_text='7 символов', max_length=7)
    passportNumber = models.CharField(verbose_name='Индентификационный номер', help_text='14 символов', max_length=14)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Клиент покупатель'
        verbose_name_plural = 'Клиенты покупатели'


class ClientSell(models.Model):
    sellerCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True)
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    address = models.CharField(verbose_name='Адресс', max_length=50)
    tel = models.IntegerField(verbose_name='Телефон')
    passportCode = models.CharField(verbose_name='Код поспорта', help_text='7 символов', max_length=7)
    passportNumber = models.CharField(verbose_name='Индентификационный номер', help_text='14 символов', max_length=14)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Клиент продавец'
        verbose_name_plural = 'Клиенты продавцы'


class Property(models.Model):
    applicationCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код заявки', primary_key=True)
    dateOfOrder = models.DateField(verbose_name='Дата составления заказа')
    name = models.CharField(verbose_name='Наименование объекта', max_length=50)
    area = models.IntegerField(verbose_name='Площадь м2')
    rooms = models.SmallIntegerField(verbose_name='Кол-во комнат')
    street = models.CharField(verbose_name='Улица', max_length=50)
    price = models.IntegerField(verbose_name='Цена')
    seller = models.ForeignKey(
        ClientSell,
        verbose_name='Продавец',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'


class SelledProperty(models.Model):
    applicationCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код заявки', primary_key=True)
    dateOfOrder = models.DateField(verbose_name='Дата составления заказа')
    name = models.CharField(verbose_name='Наименование объекта', max_length=50)
    employee = models.ForeignKey(
        Employees,
        verbose_name='Сотрудник',
        on_delete=models.CASCADE,
        null=True
    )
    seller = models.ForeignKey(
        ClientSell,
        verbose_name='Продавец',
        on_delete=models.CASCADE,
        null=True
    )
    buyer = models.ForeignKey(
        ClientBuy,
        verbose_name='Покупатель',
        on_delete=models.CASCADE,
        null=True
    )
    street = models.CharField(verbose_name='Улица', max_length=50)
    price = models.IntegerField(verbose_name='Цена')
    dateOfOperation = models.DateField(verbose_name='Дата операции')
    profit = models.IntegerField(verbose_name='Прибыль')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проданный объект'
        verbose_name_plural = 'Проданные объекты'
