# cuentas/views.py
from django.shortcuts import render

def perfil(request):
    # Aquí amor puedes pasar el contexto que necesites
    return render(request, 'cuentas/perfil.html')

def detalles_cuenta(request):
    # lógica de tu vista
    return render(request, 'cuentas/detalles.html')

def pedidos_activos(request):
    # Aquí amor puedes agregar la lógica para mostrar los pedidos activos
    return render(request, 'cuentas/pedidos.html')

def crud(request):
    # Aquí amor puedes agregar la lógica para el CRUD de cuentas
    return render(request, 'cuentas/crud.html')
