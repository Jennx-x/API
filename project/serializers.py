# Los serializers convierten los datos del modelo a formato JSON (y viceversa) para la API REST

from rest_framework import serializers #Modulo especial de rest framework
from .models import Concierto, Conferencia

class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concierto
        fields = '__all__'  # Incluye todos los campos


class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = '__all__'