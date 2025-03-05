from django.shortcuts import render, redirect
from .models import VentaManager
import json

def ventas_view(request):
    if request.method == 'POST':
        mes = request.POST.get('mes')
        venta = request.POST.get('venta')
        VentaManager.create_venta(mes, int(venta))
        return redirect('ventas')

    ventas = VentaManager.get_all_ventas()
    meses = json.dumps([venta['mes'] for venta in ventas])
    valores = json.dumps([venta['venta'] for venta in ventas])
    
    context = {
        'ventas': ventas,
        'meses': meses,
        'valores': valores
    }
    return render(request, 'ventas.html', context)