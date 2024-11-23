from rest_framework import routers
from .api import ConciertoViewSet, ConferenciaViewSet

router = routers.DefaultRouter()

# Registra las vistas con rutas únicas para cada tipo de evento
router.register('api/conciertos', ConciertoViewSet, 'conciertos')
router.register('api/conferencias', ConferenciaViewSet, 'conferencias')

urlpatterns = router.urls  # Corregido el nombre de la variable
