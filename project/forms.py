# forms.py
from django import forms
from .models import Concierto, Conferencia

class EventoForm(forms.Form):
    tipo_evento = forms.ChoiceField(
        choices=[('concierto', 'Concierto'), ('conferencia', 'Conferencia')],
        widget=forms.RadioSelect,  # Muestra las opciones como botones de radio
        required=True
    )
    nombre = forms.CharField(max_length=100)
    fecha = forms.DateTimeField()
    lugar = forms.CharField(max_length=200)

    # Campos específicos para Concierto
    artista = forms.CharField(max_length=100, required=False)
    duracion = forms.IntegerField(required=False)

    # Campos específicos para Conferencia
    tema = forms.CharField(max_length=200, required=False)
    orador = forms.CharField(max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()
        tipo_evento = cleaned_data.get('tipo_evento')

        if tipo_evento == 'concierto':
            if not cleaned_data.get('artista') or not cleaned_data.get('duracion'):
                raise forms.ValidationError("Debe ingresar el artista y la duración para el concierto.")
        elif tipo_evento == 'conferencia':
            if not cleaned_data.get('tema') or not cleaned_data.get('orador'):
                raise forms.ValidationError("Debe ingresar el tema y el orador para la conferencia.")
        
        return cleaned_data
