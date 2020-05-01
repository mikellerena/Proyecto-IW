from django.db import models


# Create your models here.

class Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField(default="01/01/1990")
    fecha_instalacion = models.DateField(default="01/01/1990")

    def __str__(self):
        return f"ID: {self.id} | Modelo: {self.modelo} | Marca: {self.marca} | Categoria: {self.categoria} | F. Adquisicion: {self.fecha_adquisicion} | F. Instalacion: {self.fecha_instalacion}"


class Empleado(models.Model):
    """Para introducir DNIs extranjeros"""
    dni = models.CharField(primary_key=True, max_length=20)
    """Por nombres compuestos"""
    nombre = models.CharField(max_length=100)
    """Dos apellidos"""
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    """Valor defecto ejemplo"""
    telefono = models.IntegerField(default=666666666)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(default="01/01/1990")

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre} | Apellidos: {self.apellidos} | Email: {self.email} | Telefono: {self.telefono} | Direccion: {self.direccion} | F. Nacimiento: {self.fecha_nacimiento}"

class Proceso(models.Model):
    """codigo_orden_fabricacion numeros y letras"""
    codigo_orden_fabricacion = models.CharField(max_length=75)
    """codigo_proceso Mezcla numeros y letras"""
    codigo_proceso = models.CharField(primary_key=True, max_length=75)
    nombre_proceso = models.CharField(max_length=100)
    """ref Mezcla numeros y letras"""
    referencia = models.CharField(max_length=75)
    fecha_inicio = models.DateField(default="01/01/1990")
    fecha_fin = models.DateField(default="01/01/1990")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f"C. Preceso: {self.codigo_proceso} | Nombre: {self.nombre_proceso} | Referencia: {self.referencia} | F. Inicio: {self.fecha_inicio} | F. Fin: {self.fecha_fin}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contraseña = models.PasswordField(max_length=200)

    def __str__(self):
        return f"Nombre: {self.nombre} | Apellidos: {self.apellidos} | Nombre de usuario: {self.nombre_usuario} | Email: {self.email}"
