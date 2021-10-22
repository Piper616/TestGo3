from django import forms


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['id_admin','persona_rut','email','contraseña']

class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['id_cargo','detalle_cargo']

class CasosForm(forms.ModelForm):
    class Meta:
        model = Casos
        fields = ['id_caso','nombre','descripcion_caso','video','audio']

class evaluacion_casoForm(forms.ModelForm):
    class Meta:
        model = EvaluacionCaso
        fields = ['id_evcaso','casos_id_caso','administrador_id_admin','evaluado_id_evaluado','fecha_asignacion','fecha_realizacion']

class evaluadorForm(forms.ModelForm):
    class Meta:
        model = Evaluador
        fields = ['id_evaluador','persona_rut','administrador_id_admin','email','contraseña']

class evaluadoForm(forms.ModelForm):
    class Meta:
        model = Evaluado
        fields = ['id_evaluado','empresa','video_respuesta','audio_respuesta','persona_rut','email','contraseña']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['rut','nombres','apellido_p','apellido_m','num_cel','email_personal','direccion','fec_nac','cargo_id_cargo']

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['id_resultado','descripcion','evaluador_id_evaluador','evaluacion_caso_id_evcaso','fecha_revision']
