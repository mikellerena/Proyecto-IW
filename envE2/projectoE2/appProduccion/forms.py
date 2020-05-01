from django import forms
from .models import Equipo, Empleado, Proceso
from django.contrib.auth.models import User


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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'date_joined'
        ]
