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


# """Formulario para registro"""
# class RegistroForm(UserCreationForm):
#     class Meta:
#         model = Usuario
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email'
#         ]
#         labels = {
#             'first_name': 'Nombre',
#             'last_name': 'Apellidos',
#             'username': 'Nombre de usuario',
#             'email': 'Email'
#         }
