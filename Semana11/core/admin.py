from django.contrib import admin
from .models import Proveedor, Producto


admin.site.register(Producto)
admin.site.register(Proveedor)
