
from django.http import HttpResponse
from django.shortcuts import render

def bienvenido(request):
    return HttpResponse('Hola mundo desde django')

def despedida(request):
    return HttpResponse('Hasta pronto')