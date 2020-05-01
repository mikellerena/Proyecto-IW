from django import forms
from .models import Equipo, Empleado, Proceso, Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


"""Formulario para registro"""
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
