from django import forms
from .models import Equipo, Empleado, Proceso


"""Formulario Equipo"""
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

"""Formulario Empleado"""
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

"""Formulario Proceso"""
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = '__all__'



