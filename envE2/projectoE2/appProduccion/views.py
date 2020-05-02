from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView, RedirectView
from django.urls import reverse_lazy
from .forms import EquipoForm, EmpleadoForm, ProcesoForm
from .models import Equipo, Empleado, Proceso

# Create your views here.
"""Clase para no poder usar las clases crear, actualizar y borrar sin iniciar sesion"""
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


"""Vista Pagina Principal"""
def principal(request):
    return render(request, 'pagina_principal.html')


"""Vista para el formulario de creacion de equipo"""
class EquipoCreateView(StaffRequiredMixin, View):
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
            return redirect('equipo_list')

        return render(request, 'create_equipo_form.html', {'form': form})


"""Vista para ver el listado de equipos"""
class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipo_list.html'
    queryset = Equipo.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(EquipoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Equipos existentes'
        return context


"""Vista para ver el detalle de los equipos"""
class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del equipo'
        return context


"""Vista para modificar los datos de los equipos"""
class EquipoUpdateView(StaffRequiredMixin, UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo_update.html'
    success_url = reverse_lazy('equipo_list')

    def get_context_data(self, **kwargs):
        context = super(EquipoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar equipos'
        return context


"""Vista para eliminar equipos"""
class EquipoDeleteView(StaffRequiredMixin, DeleteView):
    model = Equipo
    template_name = 'equipo_delete.html'
    success_url = reverse_lazy('equipo_list')


"""Vista para el formulario de creacion de empleado"""
class EmpleadoCreateView(StaffRequiredMixin, View):
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
            return redirect('empleado_list')

        return render(request, 'create_empleado_form.html', {'form': form})


"""Vista para ver el listado de empleado"""
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    queryset = Empleado.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Empleados existentes'
        return context


"""Vista para ver el detalle de los empleados"""
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        return context


"""Vista para modificar los datos de los empleados"""
class EmpleadoUpdateView(StaffRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_update.html'
    success_url = reverse_lazy('empleado_list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar empleados'
        return context


"""Vista para eliminar empleados"""
class EmpleadoDeleteView(StaffRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleado_delete.html'
    success_url = reverse_lazy('empleado_list')


"""Vista para el formulario de creación de procesos"""
class ProcesoCreateView(StaffRequiredMixin, View):
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
            return redirect('proceso_list')

        return render(request, 'create_proceso_form.html', {'form': form})


"""Vista para ver el listado de procesos"""
class ProcesoListView(ListView):
    model = Proceso
    template_name = 'proceso_list.html'
    queryset = Proceso.objects.order_by('codigo_proceso')

    def get_context_data(self, **kwargs):
        context = super(ProcesoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Procesos existentes'
        return context


"""Vista para ver el detalle de los procesos"""
class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proceso'
        return context


"""Vista para modificar los datos de los procesos"""
class ProcesoUpdateView(StaffRequiredMixin, UpdateView):
    model = Proceso
    form_class = ProcesoForm
    template_name = 'proceso_update.html'
    success_url = reverse_lazy('proceso_list')

    def get_context_data(self, **kwargs):
        context = super(ProcesoUpdateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Modificar procesos'
        return context

"""Vista para eliminar procesos"""
class ProcesoDeleteView(StaffRequiredMixin, DeleteView):
    model = Proceso
    template_name = 'proceso_delete.html'
    success_url = reverse_lazy('proceso_list')

"""Vista para que el usuario pueda cerrar sesión"""
class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'login'
    
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
