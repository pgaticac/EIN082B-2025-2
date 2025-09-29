from django.shortcuts import render, HttpResponse

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
    return render(request,'core/contacto.html')