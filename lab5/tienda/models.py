from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.FloatField()
    telefono = models.FloatField()
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    fecha_de_nacimiento = models.DateTimeField
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre    