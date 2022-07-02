from django.shortcuts import render
from django.http import HttpResponse




def familiar(request):
    return HttpResponse('familiar: ')


def familiar_a(request,nombre):
    return HttpResponse(f'se llama {nombre}')