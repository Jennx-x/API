from django.db import models
from datetime import datetime

class BaseEvento(models.Model):
    """
    Clase abstracta que representa los atributos y métodos comunes
    para diferentes tipos de eventos.
    """
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)

    def mostrar_info(self):
        """
        Método para mostrar información básica de un evento.
        """
        return f"Evento: {self.nombre}, Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}, Lugar: {self.lugar}"

    @staticmethod
    def es_evento_proximo(fecha_evento):
        """
        Método estático para verificar si un evento es próximo
        (es decir, su fecha es mayor a la actual).
        """
        return fecha_evento > datetime.now()

    @classmethod
    def crear_evento(cls, nombre, fecha, lugar):
        """
        Método de clase para crear instancias de eventos.
        """
        return cls(nombre=nombre, fecha=fecha, lugar=lugar)

    class Meta:
        abstract = True  # Declara la clase como abstracta


class Concierto(BaseEvento):
    """
    Modelo que representa un concierto, hereda de BaseEvento.
    """
    artista = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")

    def mostrar_info(self):
        """
        Método sobrescrito para mostrar información específica de un concierto.
        """
        base_info = super().mostrar_info()  # Llama al método de la clase base
        return f"{base_info}, Artista: {self.artista}, Duración: {self.duracion} minutos"


class Conferencia(BaseEvento):
    """
    Modelo que representa una conferencia, hereda de BaseEvento.
    """
    tema = models.CharField(max_length=200)
    orador = models.CharField(max_length=100)

    def mostrar_info(self):
        """
        Método sobrescrito para mostrar información específica de una conferencia.
        """
        base_info = super().mostrar_info()  # Llama al método de la clase base
        return f"{base_info}, Tema: {self.tema}, Orador: {self.orador}"
