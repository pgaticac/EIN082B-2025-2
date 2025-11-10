from core.models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields= "__all__"
        # fields = ["codigo","descripcion","precio"]
        # exclude = ["codigo"]