from django.db import models


class Employees(models.Model):
    code = models.IntegerField('Код')
    FIO = models.CharField('ФИО', max_length=50)
    post = models.CharField('Должность', max_length=50)
    dateOfEmployment = models.DateField('Дата найма', )
    address = models.CharField('Адресс', max_length=50)
    tel = models.IntegerField('Телефон', )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
