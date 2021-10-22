from .models import Evaluado, Evaluador, Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class EvaluadoSerializer(serializers.ModelSerializer):
    def validar_email(self, value):
        existe = Evaluado.objects.filter(email__iexact=value).exist()

        if existe:
            raise serializers.ValidationError("Este rut ya existe")
        return value

    class Meta:
        model = Evaluado
        fields = '__all__'
        #exclude : por si no quiero algo en especifico

class EvaluadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluador
        fields = '__all__'
        #exclude : por si no quiero algo en especifico
