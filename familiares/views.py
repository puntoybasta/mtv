from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from familiares.models import Familiar




def familiar(request):
    return HttpResponse('familiar: ')


def familiar_a(request,nombre):
    return HttpResponse(f'se llama {nombre}')

def datos_personales(request):
    
    context = {}
    if request.GET:
        context['nombre'] = request.GET['nombre']

    return render(request,'familiares/index.html', context)


def listar_familiares(request):
    context = {}
    context['familiares'] = Familiar.objects.all()
    return render(request, 'familiares/listar_familiares.html',context)
