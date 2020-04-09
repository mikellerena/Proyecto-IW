from django.shortcuts import render, redirect
from django.views import View
from .forms import EquipoForm, EmpleadoForm, ProcesoForm
from .models import Equipo ,Empleado, Proceso

# Create your views here.

class CreateEquipoView(View):
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de empleados'
        }
        return render(request, 'create_equipo_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')

        return render(request, 'create_equipo_form.html', {'form': form})
