from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Employees(models.Model):
    employeeCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True, )
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    post = models.CharField(verbose_name='Должность', max_length=50)
    dateOfEmployment = models.DateField(verbose_name='Дата найма')
    address = models.CharField(verbose_name='Адрес', max_length=50)
    tel = IntegerRangeField(verbose_name='Телефон', min_value=1, max_value=999999)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class ClientBuy(models.Model):
    buyerCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True)
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    tel = IntegerRangeField(verbose_name='Телефон', min_value=1, max_value=999999)
    passportCode = models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Длинна = 9', code='nomatch')],
                                    verbose_name='Код поспорта',
                                    help_text='2 буквы и 7 цифр',
                                    max_length=9,
                                    unique=True)
    passportNumber = models.CharField(validators=[RegexValidator(regex='^.{14}$', message='Длинна = 14', code='nomatch')],
                                      verbose_name='Индентификационный номер',
                                      help_text='14 символов',
                                      max_length=14,
                                      unique=True)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Клиент покупатель'
        verbose_name_plural = 'Клиенты покупатели'


class ClientSell(models.Model):
    sellerCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код', primary_key=True)
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    tel = IntegerRangeField(verbose_name='Телефон', min_value=1, max_value=999999)
    passportCode = models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Длинна = 9', code='nomatch')],
                                    verbose_name='Код поспорта',
                                    help_text='2 буквы и 7 цифр',
                                    max_length=9,
                                    unique=True)
    passportNumber = models.CharField(validators=[RegexValidator(regex='^.{14}$', message='Длинна = 14', code='nomatch')],
                                      verbose_name='Индентификационный номер',
                                      help_text='14 символов',
                                      max_length=14,
                                      unique=True)

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
    address = models.CharField(verbose_name='Адрес', max_length=50)
    price = models.IntegerField(verbose_name='Цена')
    seller = models.ForeignKey(
        ClientSell,
        verbose_name='Продавец',
        on_delete=models.CASCADE,
        null=True
    )
    ifSelled = models.BooleanField(verbose_name='Состояние продажи', default=False)

    def __str__(self):
        return '%s (%s)' % (self.name, self.applicationCode)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'

    def save(self, *args, **kwargs):
        super(Property, self).save(*args, **kwargs)


class SelledProperty(models.Model):
    contractCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код договора', primary_key=True)
    applicationCode = models.ForeignKey(
        Property,
        verbose_name='Код заявки',
        on_delete=models.CASCADE,
        null=True
    )
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
    dateOfOperation = models.DateField(verbose_name='Дата операции')
    profit = models.IntegerField(verbose_name='Прибыль')

    def __str__(self):
        a = self.contractCode
        return str(a)

    class Meta:
        verbose_name = 'Совершенная сделка'
        verbose_name_plural = 'Совершенные сделки'

    def save(self, *args, **kwargs):
        super(SelledProperty, self).save(*args, **kwargs)



'''

@receiver(post_save, sender=SelledProperty, dispatch_uid="update_property")
def update_property(sender, created, instance, **kwargs):
        #x1 = instance.applicationCode.find("(")
        #x2 = instance.applicationCode.find(")")
        #x = instance.applicationCode[x1+1: x2]
        if created:
            property = Property.objects.get(applicationCode = instance.applicationCode)
            property.ifSelled=True
            property.save()




def profile_thumbanil(sender, created, instance , update_fields=["thumbnail_image"], **kwargs):
    profile = UserProfile.objects.get(id = instance.id)
    thumb = handlers.create_thumbanil(profile.image, profile.user_id)
    profile.update(thumbnail_image = thumb)

post_save.connect(profile_thumbanil, sender=UserProfile)
'''