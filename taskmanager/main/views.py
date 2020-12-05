from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html')


def tables(request):
    return render(request, 'main/tables.html')


