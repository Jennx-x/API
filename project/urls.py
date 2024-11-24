from rest_framework import routers
from django.urls import path, include  # Asegúrate de importar 'include'
from . import views
from .api import ConciertoViewSet, ConferenciaViewSet

# Registrar las vistas para la API
router = routers.DefaultRouter()
router.register('conciertos', ConciertoViewSet, 'conciertos')
router.register('conferencias', ConferenciaViewSet, 'conferencias')

urlpatterns = [
    # Rutas para la aplicación web (CRUD tradicional)
    path('', views.index, name='index'),  # Página principal con el CRUD
    path('crear/', views.crear_evento, name='crear_evento'),  # Crear evento (POST)
    path('listar/', views.listar_evento, name='listar_evento'),  # Listar eventos (GET)
    path('actualizar/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),  # Actualizar evento (PUT)
    path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),  # Eliminar evento (DELETE)

    # Incluir las rutas de la API
    path('api/', include(router.urls))  # Incluir las rutas de la API REST generadas por el router
]
