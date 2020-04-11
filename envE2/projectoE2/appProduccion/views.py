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
    template_name = 'equipos_list.html'
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


"""Vista para el formulario de creacion de empleado"""


class CreateEmpleadoView(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de empleados'
        }
        return render(request, 'create_empleado_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

        return render(request, 'create_empleado_form.html', {'form': form})


"""Vista para ver el listado de empleado"""


class EmpleadosListView(ListView):
    model = Empleado
    template_name = 'empleados_list.html'
    queryset = Empleado.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Empleados existentes'
        return context


"""Vista para ver el detalle de los empleados"""


class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los empleados'
        return context

<<<<<<< HEAD
=======

>>>>>>> master
"""Vista para el formulario de creación de procesos"""


class CreateProcesoView(View):
    def get(self, request, *args, **kwargs):
        form = ProcesoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Apartado para la creación de procesos'
        }
        return render(request, 'create_proceso_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('procesos')

        return render(request, 'create_proceso_form.html', {'form': form})


"""Vista para ver el listado de procesos"""


class ProcesosListView(ListView):
    model = Proceso
    template_name = 'procesos_list.html'
    queryset = Proceso.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ProcesosListView, self).get_context_data(**kwargs)
        context['titulo_pagin'] = 'Procesos existentes'
        return context


"""Vista para ver el detalle de los procesos"""


class ProcesosDetailView(DetailView):
    model = Proceso
    template_name = 'procesos_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesosDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de los procesos'
        return context
