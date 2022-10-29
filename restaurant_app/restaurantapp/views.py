from ast import For
from cgitb import reset
from csv import reader
from tkinter.tix import Form
from urllib import request
from datetime import date, timezone
from restaurantapp.models import reservas
from restaurantapp.forms import FormProyecto
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

def listaRSV(request):
    reserva = reservas.objects.all()
    data = {'reserva': reserva}
    return render(request,'reservas.html', data)


def agr_reserva(request):
    form=FormProyecto()
    if request.method=='POST':
        form=FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render (request, 'agregarResv.html',data)

def actaulizar_reserva(request, id):
    Res= reservas.objects.get(id=id)
    form=FormProyecto(instance=Res)
    if request.method=='POST':
        form=FormProyecto(request.POST, instance=Res)
        if form.is_valid():
            form.save()
            return index (request)
    data={'form':form}
    return render (request, 'agregarResv.html',data)

def quitar_reserva(request, id):
    Res=reservas.objects.get(id=id)
    Res.delete()
    return redirect('/reservas')







