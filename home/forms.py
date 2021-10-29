from typing import Pattern
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
import datetime


class evaluadoForm(forms.ModelForm):
    class Meta:
        model = Evaluado

        fields =[
            'id_evaluado', 
            'rut_evaluado',
            'nombres',
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
            'id_evaluado':'Identificación', 
            'rut_evaluado': 'Rut',
            'nombres': 'Nombres',
            'apellido_p':'Apellido Paterno',
            'apellido_m':'Apellido Materno',
            'num_cel':'Número celular',
            'email_personal':'Email Personal',
            'direccion':'Dirección',
            'fec_nac':'Fecha de Nacimiento',
            'empresa':'Empresa',
            'email_empresa': 'Email Empresarial',
            'contraseña':'Contraseña',
            'cargo_id_cargo':'Cargo'
        }

        widgets = {
            'id_evaluador': forms.TextInput(attrs={'class':'form-control'}), 
            'rut_evaluador': forms.NumberInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class':'form-control'}),
            'num_cel': forms.NumberInput(attrs={'class':'form-control'}),
            'email_personal': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fec_nac': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'email_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'cargo_id_cargo': forms.Select(attrs={'class':'form-control'})
        }
    
class evaluadorForm(forms.ModelForm):
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
            'id_evaluador':'Identificación', 
            'rut_evaluador': 'Rut',
            'nombres': 'Nombres',
            'apellido_p':'Apellido Paterno',
            'apellido_m':'Apellido Materno',
            'num_cel':'Número celular',
            'email_personal':'Email Personal',
            'direccion':'Dirección',
            'fec_nac':'Fecha de Nacimiento',
            'administrador_id_admin':'Administrador a cargo',
            'email_empresa': 'Email Empresarial',
            'contraseña':'Contraseña',
            'cargo_id_cargo':'Cargo'
        }

        widgets = {
            'id_evaluador': forms.TextInput(attrs={'class':'form-control'}), 
            'rut_evaluador': forms.NumberInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class':'form-control'}),
            'num_cel': forms.NumberInput(attrs={'class':'form-control'}),
            'email_personal': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fec_nac': forms.TextInput(attrs={'class':'form-control'}),
            'administrador_id_admin': forms.Select(attrs={'class':'form-control'}),
            'email_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'cargo_id_cargo': forms.Select(attrs={'class':'form-control'})
        }

class actividadForm(forms.ModelForm):
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
            'id_caso':'Número',
            'nombre': 'Nombre Actividad',
            'descripcion_caso': 'Descripción',
            'foto': 'Imagen',
            'video' : 'Video'
        }

        widgets = {
            'id_caso': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion_caso': forms.TextInput(attrs={'class':'form-control'}),
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
