from django.shortcuts import render, HttpResponse

def home(request):
    titulo = "<h1>Home</h1>"
    #return HttpResponse(titulo)
    return render(request,'core/home.html')
    
def contacto(request):
    titulo = "<h1>Contacto</h1>"
    return HttpResponse(titulo)