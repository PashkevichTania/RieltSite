# Generated by Django 3.1.3 on 2020-12-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201205_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBuy',
            fields=[
                ('code', models.IntegerField(help_text='Код', primary_key=True, serialize=False)),
                ('FIO', models.CharField(help_text='ФИО', max_length=50)),
                ('address', models.CharField(help_text='Адресс', max_length=50)),
                ('tel', models.IntegerField(help_text='Телефон')),
                ('passportNumber', models.CharField(help_text='Код поспорта', max_length=50)),
                ('passportCode', models.CharField(help_text='Индентификационный номер', max_length=50)),
            ],
            options={
                'verbose_name': 'Клиент покупатель',
                'verbose_name_plural': 'Клиенты покупатели',
            },
        ),
        migrations.CreateModel(
            name='ClientSell',
            fields=[
                ('code', models.IntegerField(help_text='Код', primary_key=True, serialize=False)),
                ('FIO', models.CharField(help_text='ФИО', max_length=50)),
                ('address', models.CharField(help_text='Адресс', max_length=50)),
                ('tel', models.IntegerField(help_text='Телефон')),
                ('passportNumber', models.CharField(help_text='Код поспорта', max_length=50)),
                ('passportCode', models.CharField(help_text='Индентификационный номер', max_length=50)),
            ],
            options={
                'verbose_name': 'Клиент продавец',
                'verbose_name_plural': 'Клиенты продавцы',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('applicationCode', models.IntegerField(help_text='Код заявки', primary_key=True, serialize=False)),
                ('dateOfOrder', models.DateField(help_text='Дата составления заказа')),
                ('name', models.CharField(help_text='Наименование объекта', max_length=50)),
                ('area', models.IntegerField(help_text='Площадь м2')),
                ('rooms', models.IntegerField(help_text='Кол-во комнат')),
                ('street', models.CharField(help_text='Улица', max_length=50)),
                ('price', models.IntegerField(help_text='Цена')),
                ('sellerCode', models.IntegerField(help_text='Код продавца')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимость',
            },
        ),
        migrations.CreateModel(
            name='SelledProperty',
            fields=[
                ('applicationCode', models.IntegerField(help_text='Код заявки', primary_key=True, serialize=False)),
                ('dateOfOrder', models.DateField(help_text='Дата составления заказа')),
                ('name', models.CharField(help_text='Наименование объекта', max_length=50)),
                ('employeeCode', models.IntegerField(help_text='Код сотрудника')),
                ('sellerCode', models.IntegerField(help_text='Код продавца')),
                ('buyerCode', models.IntegerField(help_text='Код покупателя')),
                ('street', models.CharField(help_text='Улица', max_length=50)),
                ('price', models.IntegerField(help_text='Цена')),
                ('dateOfOperation', models.DateField(help_text='Дата операции')),
                ('profit', models.IntegerField(help_text='Прибыль')),
            ],
            options={
                'verbose_name': 'Проданный объект',
                'verbose_name_plural': 'Проданные объекты',
            },
        ),
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.AlterField(
            model_name='employees',
            name='FIO',
            field=models.CharField(help_text='ФИО', max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.CharField(help_text='Адресс', max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='code',
            field=models.IntegerField(help_text='Код', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employees',
            name='dateOfEmployment',
            field=models.DateField(help_text='Дата найма'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='post',
            field=models.CharField(help_text='Должность', max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='tel',
            field=models.IntegerField(help_text='Телефон'),
        ),
    ]
