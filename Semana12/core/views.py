from django.shortcuts import render, HttpResponse
from .models import Contacto

def home(request):
    titulo = "Inicio"

    productos = ['computadores','periféricos','servidores']
    
    data = {
        "titulo": titulo,
        "productos":productos
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