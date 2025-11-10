from rest_framework import routers
from .views import ProductoViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('productos',ProductoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]