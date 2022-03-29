from django.shortcuts import redirect, render
from .models import Permanente, Freelance, Administrativo
from .forms import PermanenteFormulario, FreelanceFormulario, AdministrativoFormulario, PermanenteBuscar, FreelanceBuscar, AdministrativoBuscar

def crear_permanente(request):
    if request.method == 'POST':
        form = PermanenteFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            permanente = Permanente(nombre=data['nombre'], apellido=data['apellido'], area=data['area'], desempleado=data['desempleado'], sueldo_aportes=data['sueldo_aportes'])
            permanente.save()
            # return render(request,'index/index.html', {})
            return redirect ('index')       
    
    form = PermanenteFormulario()
    return render(request, 'profesionales/crear_permanente.html', {'form':form})

def crear_freelance(request):
    if request.method == 'POST':
        form = FreelanceFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            freelance = Freelance(nombre=data['nombre'], apellido=data['apellido'], area=data['area'], desempleado=data['desempleado'], tarea_asignada=data['tarea_asignada'], fecha_entrega=data['fecha_entrega'])
            freelance.save()
            # return render(request,'index/index.html', {})
            return redirect ('index')
    
    form = FreelanceFormulario()
    return render(request, 'profesionales/crear_freelance.html', {'form':form})

def crear_administrativo(request):   
    if request.method == 'POST':
        form = AdministrativoFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            administrativo = Administrativo(nombre=data['nombre'], apellido=data['apellido'], antiguedad=data['antiguedad'], desempleado=data['desempleado'])
            administrativo.save()
            # return render(request,'index/index.html', {})
            return redirect ('index')
     
    form = AdministrativoFormulario()
    return render(request, 'profesionales/crear_administrativo.html', {'form':form})


def lista_permanentes(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    if nombre_a_buscar is not None:
        permanentes = Permanente.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        permanentes = Permanente.objects.all()
    permanentes=None
    form = PermanenteBuscar()
    return render(request, 'profesionales/lista_permanentes.html', {'form':form, 'permanentes': permanentes})

def lista_freelances(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    if nombre_a_buscar is not None:
        freelances = Freelance.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        freelances = Freelance.objects.all()
    freelances=None
    form = FreelanceBuscar()
    return render(request, 'profesionales/lista_freelances.html', {'form':form, 'freelances': freelances})

def lista_administrativos(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    if nombre_a_buscar is not None:
        administrativos = Administrativo.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        administrativos = Administrativo.objects.all()
    administrativos=None
    form = AdministrativoBuscar()
    return render(request, 'profesionales/lista_administrativos.html', {'form':form, 'administrativos': administrativos})

