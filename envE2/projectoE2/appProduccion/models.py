from django.db import models


# Create your models here.

class Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()

    def __str__(self):
        return f"ID: {self.id}, Modelo: {self.modelo}, Marca: {self.marca}, Categoria: {self.categoria}, F. Adquisicion: {self.fecha_adquisicion}, F. Instalacion: {self.fecha_instalacion}"


class Empleado(models.Model):
    """Para introducir DNIs extranjeros"""
    dni = models.CharField(primary_key=True, max_length=20)
    """Por nombres compuestos"""
    nombre = models.CharField(max_length=100)
    """Dos apellidos"""
    apellidos = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    """Valor defecto ejemplo"""
    telefono = models.IntegerField(default=666666666)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Email: {self.email}, Telefono: {self.telefono}, Direccion: {self.direccion}, F. Nacimiento: {self.fecha_nacimiento}"

class Orden(models.Model):
    """codigo_orden_fabricacion numeros y letras"""
    codigo = models.CharField(primary_key=True, max_length=75)
    """Entidad que contrata los servicios"""
    cliente = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    #procesos = models.ManyToManyField(Proceso)

    def __str__(self):
        return f"Codigo: {self.codigo}, Cliente: {self.cliente}, F. Inicio: {self.fecha_inicio}"

class Proceso(models.Model):
    """codigo_orden_fabricacion numeros y letras, foreign key"""
    codigo_orden_fabricacion = models.ForeignKey(Orden, on_delete=models.CASCADE)
    """codigo_proceso Mezcla numeros y letras"""
    codigo_proceso = models.CharField(primary_key=True, max_length=75)
    nombre_proceso = models.CharField(max_length=100)
    """ref Mezcla numeros y letras"""
    referencia = models.CharField(max_length=75)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f"C. Preceso: {self.codigo_proceso}, Nombre: {self.nombre_proceso}, Referencia: {self.referencia}, F. Inicio: {self.fecha_inicio}, F. Fin: {self.fecha_fin}"


