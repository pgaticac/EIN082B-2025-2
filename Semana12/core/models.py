from django.db import models

class Proveedor(models.Model):
    rut = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Provedores"

class Producto(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,models.SET_NULL, null=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre +" - " + self.mensaje

