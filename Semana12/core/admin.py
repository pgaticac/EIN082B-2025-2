from django.contrib import admin
from .models import Proveedor, Producto, Contacto


admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Contacto)
