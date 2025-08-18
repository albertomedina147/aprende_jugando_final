from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MensajeContacto  # Importar el modelo

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Guardar el mensaje en la base de datos
        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )
        messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
        return redirect('contacto')  # Asegúrate de tener esta URL con name="contacto"

    return render(request, 'contacto.html')

def acerca_de(request):
   return render(request, 'acerca.html')

def catalogo(request):
    return render(request, 'catalogo/catalogo.html')
