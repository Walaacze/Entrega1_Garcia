from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})


def plantilla(request):
    datos = {
        'lista': ['administrativo', 'permanente', 'freelance'],
    }
    return render(request, 'index/plantilla.html', datos)