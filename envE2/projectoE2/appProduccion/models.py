from django.db import models

# Create your models here.

class Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    f_adquisicion = models.DateField()
    f_intalacion = models.DateField()

    def __str__(self):
        return f"ID: {self.id}, Modelo: {self.modelo}, Marca: {self.marca}, Categoria: {self.categoria}, F. Adquisicion: {self.f_adquisicion}, F. Instalacion: {self.f_intalacion}"

class Empleado(models.Model):
    dni = models.CharField(primary_key=True, max_length=20) #Para introducir DNIs extranjeros
    nombre = models.CharField(max_length=100) #Por nombres compuestos
    apellidos = models.CharField(max_length=150) #Dos apellidos
    email = models.CharField(max_length=100)
    tel = models.IntegerField(default=666666666) #Valor defecto ejemplo
    dir = models.CharField(max_length=150)
    f_nacimiento = models.DateField()

    def __str__(self):
        return f"ID: {self.id}, DNI: {self.dni}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Email: {self.email}, Telefono: {self.tel}, Direccion: {self.dir}, F. Nacimiento: {self.f_nacimiento}"

class Proceso(models.Model):
    cof = models.CharField(max_length=75) #Mezcla numeros y letras
    cp = models.CharField(primary_key=True, max_length=75) #Mezcla numeros y letras
    nom_pro = models.CharField(max_length=100)
    ref = models.CharField(max_length=75) #Mezcla numeros y letras
    f_inicio = models.DateField()
    f_fin = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f"ID: {self.id}, Codigo OF: {self.cof}, C. Preceso: {self.cp}, Nombre: {self.nom_pro}, Referencia: {self.ref}, F. Inicio: {self.f_inicio}, F. Fin: {self.f_fin}"
