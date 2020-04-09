from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .forms import EquipoForm, EmpleadoForm, ProcesoForm
from .models import Equipo ,Empleado, Proceso

# Create your views here.

"""Vista para el formulario de creacion de equipo"""
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

"""Vista para ver el listado de equipos"""
class EquiposListView(ListView):
    model = Equipo
    template_name = 'equipos.html'
    queryset = Equipo.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(EquiposListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Equipos existentes'
        return context
