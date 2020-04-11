from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .forms import EquipoForm, EmpleadoForm, ProcesoForm
from .models import Equipo, Empleado, Proceso

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

"""Vista para ver el detalle de los equipos"""
class EquiposDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquiposDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los equipos'
        return context

<<<<<<< HEAD
=======
"""Vista para el formulario de creacion de empleado"""
class CreateEmpleadoView(View):
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de empleados'
        }
        return render(request, 'create_empleado_form.html', context)

    def post(self, request, *args, **kwargs):
        form = Empleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

        return render(request, 'create_empleado_form.html', {'form': form})

"""Vista para ver el listado de empleado"""
class EmpleadosListView(ListView):
    model = Empleado
    template_name = 'empleados.html'
    queryset = Empleado.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Empleado, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Empleados existentes'
        return context

"""Vista para ver el detalle de los empleados"""
class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = 'empleados.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los empleados'
        return context

>>>>>>> master
