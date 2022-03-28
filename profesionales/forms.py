from django import forms

class PermanenteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    area = forms.CharField(max_length=40)
    desempleado = forms.BooleanField(required=False)
    sueldo_aportes = forms.IntegerField(max_value=1000000)
    
class FreelanceFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    area = forms.CharField(max_length=40)
    desempleado = forms.BooleanField(required=False)
    tarea_asignada = forms.CharField(max_length=35)
    fecha_entrega = forms.DateTimeField()


class AdministrativoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    antigüedad = forms.DateField()
    desempleado = forms.BooleanField(required=False)   
    
    
class PermanenteBuscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class FreelanceBuscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class AdministrativoBuscar(forms.Form):
    nombre = forms.CharField(max_length=20)
