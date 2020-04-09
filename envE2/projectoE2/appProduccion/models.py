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
    tel = models.IntegerField(default=666666666)
    dir = models.CharField(max_length=150)
    f_nacimiento = models.DateField()

    def __str__(self):
        return f"ID: {self.id}, DNI: {self.dni}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Email: {self.email}, Telefono: {self.tel}, Direccion: {self.dir}, F. Nacimiento: {self.f_nacimiento}"

class Proceso(models.Model):
    """ cof numeros y letras"""
    cof = models.CharField(max_length=75)
    """ cp Mezcla numeros y letras"""
    cp = models.CharField(primary_key=True, max_length=75)
    nom_pro = models.CharField(max_length=100)
    """ ref Mezcla numeros y letras"""
    ref = models.CharField(max_length=75)
    f_inicio = models.DateField()
    f_fin = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f"ID: {self.id}, Codigo OF: {self.cof}, C. Preceso: {self.cp}, Nombre: {self.nom_pro}, Referencia: {self.ref}, F. Inicio: {self.f_inicio}, F. Fin: {self.f_fin}"
