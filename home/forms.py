from typing import Pattern
from django import forms
from django.core.exceptions import ViewDoesNotExist
from django.db.models import fields
from django.forms import widgets
from .models import *
import datetime
from django.forms import ValidationError
from .validators import *


class evaluadoForm(forms.ModelForm):

    def clean_rut(self, rut):
        rut = self.cleaned_data["rut_evaluador"]
        existe = Evaluador.objects.filter(rut_evaluador=rut).exists()

        if existe:
            print("Esta funcionando")
            raise ValidationError("Este rut ya existe")

        return rut

    id_evaluado = forms.CharField(label='Id', widget = forms.TextInput(attrs={"placeholder":"Ingrese Id"}))
    rut_evaluado = forms.CharField(label='Rut Evaluado', widget = forms.TextInput(attrs={"placeholder":"ej: 11.111.111-1"}))
    nombre = forms.CharField(label='Nombre/s', widget = forms.TextInput(attrs={"placeholder":"Ingrese Nombre/s del evaluado"}))
    apellido_p = forms.CharField(label='Apellido Paterno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido paterno"}))
    apellido_m = forms.CharField(label='Apellido Materno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido materno"}))
    num_cel = forms.CharField(label='Número de celular', widget = forms.TextInput(attrs={"placeholder":"Ej: 9 999 99 999"}))
    email_personal = forms.CharField(label='Email Personal', widget = forms.TextInput(attrs={"placeholder":"ej: persona@personal.com"}))
    direccion = forms.CharField(label='Dirección', widget = forms.TextInput(attrs={"placeholder":"Ingres dirección del evaluado"}))
    fec_nac = forms.CharField(label='Fecha de Nacimiento', widget = forms.TextInput(attrs={"placeholder":"Ingrese fecha de nacimiento del evaluado"}))
    empresa = forms.CharField(label='Empresa perteneciente', widget = forms.TextInput(attrs={"placeholder":"Ingrese empresa del evaluado"}))
    email_empresa = forms.CharField(label='Email contacto empresa', widget = forms.TextInput(attrs={"placeholder":"ej: persona@empresa.cl"}))
    contraseña = forms.CharField(label='Contraseña', widget = forms.TextInput(attrs={"placeholder":"Ingrese contraseña para ingreso"}))

    class Meta:
        model = Evaluado

        fields =[
            'id_evaluado', 
            'rut_evaluado',
            'nombre',
            'apellido_p',
            'apellido_m',
            'num_cel',
            'email_personal',
            'direccion',
            'fec_nac',
            'empresa',
            'email_empresa',
            'contraseña',
            'cargo_id_cargo'
        ]

        labels = {
            'cargo_id_cargo':'Cargo'
        }

        widgets = {
            'cargo_id_cargo': forms.Select(attrs={'class':'form-control'})
        }
    
class evaluadorForm(forms.ModelForm):
   
    def clean_rut(self, rut):
        rut = self.cleaned_data["rut_evaluador"]
        existe = Evaluador.objects.filter(rut_evaluador=rut).exists()

        if existe:
            print("Esta funcionando")
            raise ValidationError("Este rut ya existe")

        return rut

    id_evaluador = forms.CharField(label='Identificación', widget = forms.TextInput(attrs={"placeholder":"Ingrese Id"}))
    rut_evaluador = forms.CharField(label='Rut', widget = forms.TextInput(attrs={"placeholder":"ej: 11.111.111-1"}))
    nombres = forms.CharField(label='Nombres' , widget = forms.TextInput(attrs={"placeholder":"Ingrese nombre/s del evaluador"}))
    apellido_p = forms.CharField(label='Apellido Paterno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido paterno"}))
    apellido_m = forms.CharField(label='Apellido Materno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido materno"}))
    num_cel = forms.CharField(label='Número de celular', widget = forms.NumberInput(attrs={"placeholder":"ej: 9 999 999 99"}))
    email_personal = forms.CharField(label='Email Personal', widget = forms.TextInput(attrs={"placeholder":"ej: ejemplo@ejemplo.com"}))
    direccion = forms.CharField(label='Dirección', widget = forms.TextInput(attrs={"placeholder":"Ingrese su Dirección actual"}))
    fec_nac = forms.CharField(label='Fecha de Nacimiento', widget = forms.TextInput(attrs={"placeholder":"Fecha de nacimiento"}))
    email_empresa = forms.CharField(label='Email empresa', widget = forms.TextInput(attrs={"placeholder":"ej: empresa@ejemplo.com"}))
    contraseña = forms.CharField(label='Contraseña', widget = forms.TextInput(attrs={"placeholder":"Ingrese contraseña"}))

    class Meta:
        model = Evaluador

        fields = [
            'id_evaluador', 
            'rut_evaluador',
            'nombres',
            'apellido_p',
            'apellido_m',
            'num_cel',
            'email_personal',
            'direccion',
            'fec_nac',
            'administrador_id_admin',
            'email_empresa',
            'contraseña',
            'cargo_id_cargo'
        ]

        labels = {
            'administrados_id_admin' : 'Administrador a cargo',
            'cargo_id_cargo' : 'Cargo actual'
        }
    
        widgets = {
            'administrador_id_admin': forms.Select(attrs={'class':'form-control'}),
            'cargo_id_cargo': forms.Select(attrs={'class':'form-control'})
        }


class actividadForm(forms.ModelForm):

    id_caso = forms.CharField(label='Identificación', widget = forms.TextInput(attrs={"placeholder":"Número de identificación"}))
    nombre = forms.CharField(label='Nombre', widget = forms.TextInput(attrs={"placeholder":"Nombre del caso"}))
    descripcion_caso = forms.CharField(label='Descripción', widget = forms.TextInput(attrs={"placeholder":"Descripción del caso"}))

    class Meta:
        model = Casos

        fields = [
            'id_caso',
            'nombre',
            'descripcion_caso',
            'foto',
            'video'
        ]

        labels = {
            'foto': 'Imagen',
            'video' : 'Video'
        }

        widgets = {
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'video': forms.FileInput(attrs={'class':'form-control'})
        }

class asignarForm(forms.ModelForm):
    class Meta:
        model = EvaluacionCaso

        fields = [
            'id_evcaso',
            'casos_id_caso',
            'administrador_id_admin',
            'evaluado_id_evaluado',
            'fecha_asignacion'
        ]

        labels = {
            'id_evcaso': 'Número de Evaluación',
            'casos_id_caso': 'Número del Caso',
            'administrador_id_admin': 'Identificador de Administrador',
            'evaluado_id_evaluado': 'Identficación Evaluado',
            'fecha_asignacion' : 'Fecha de la asignación'
        }

        widgets = {
            'id_evcaso': forms.TextInput(attrs={'class':'form-control'}),
            'casos_id_caso': forms.Select(attrs={'class':'form-control'}),
            'administrador_id_admin': forms.Select(attrs={'class':'form-control'}),
            'evaluado_id_evaluado': forms.Select(attrs={'class':'form-control'}),
            'fecha_asignacion': forms.DateInput(format='%d/%m/%Y')
        }
