from django.shortcuts import render, HttpResponse
import requests
from .models import Contacto

def home(request):
    #Lectura de API de Terceros 
    
    #Clima Viña
    url_api = "https://api.gael.cloud/general/public/clima/SCVM"
    conexion_api = requests.get(url_api)
    datos_api = conexion_api.json()
    
    productos_api = "https://fakestoreapi.com/products"
    c = requests.get(productos_api)
    productos = c.json()
    
    titulo = "Inicio"

    
    
    data = {
        "titulo": titulo,
        "productos":productos,
    }
     
    #return HttpResponse(titulo)
    return render(request,'core/home.html',data)
    
def contacto(request):
    titulo = "Contacto"

    if request.POST:
        #capturar el mensaje
        nombre = request.POST["txtNombre"]
        email = request.POST["txtEmail"]
        mensaje = request.POST["txtMensaje"]

        #validaciones de negocio

        #crear nuevo objeto
        nuevoContacto = Contacto()
        nuevoContacto.nombre = nombre
        nuevoContacto.email = email
        nuevoContacto.mensaje = mensaje

        nuevoContacto.save()



    return render(request,'core/contacto.html')