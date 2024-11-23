from .models import Concierto, Conferencia  # Importa los modelos
from rest_framework import viewsets  # Importa las vistas de Django REST Framework
from rest_framework.permissions import IsAuthenticated  # Permiso para autenticación
from .serializers import ConciertoSerializer, ConferenciaSerializer  # Corrige el nombre del archivo

class ConciertoViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar los conciertos (CRUD).
    """
    queryset = Concierto.objects.all()  # Consulta todos los conciertos
    serializer_class = ConciertoSerializer  # Usa el serializador de conciertos
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

class ConferenciaViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar las conferencias (CRUD).
    """
    queryset = Conferencia.objects.all()  # Consulta todas las conferencias
    serializer_class = ConferenciaSerializer  # Usa el serializador de conferencias
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

