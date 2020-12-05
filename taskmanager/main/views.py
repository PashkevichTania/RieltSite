from django.shortcuts import render, redirect
from .models import Employees
import pyodbc


def index(request):
    return render(request, 'main/index.html')


def tables(request):
    employees = Employees.objects.all()
    return render(request, 'main/tables.html', {'employees': employees})


def sql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=LOL\SQLEXPRESS;'
                          'Database=Rielt;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("select * from Сотрудники")
    result = cursor.fetchall()
    return render(request, 'main/sql.html', {Employees: result})

