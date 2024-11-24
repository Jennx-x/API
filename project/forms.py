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

    # Campos específicos para Concierto (solo visibles cuando se selecciona "Concierto")
    artista = forms.CharField(max_length=100, required=False)
    duracion = forms.IntegerField(required=False)

    # Campos específicos para Conferencia (solo visibles cuando se selecciona "Conferencia")
    tema = forms.CharField(max_length=200, required=False)
    orador = forms.CharField(max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()
        tipo_evento = cleaned_data.get('tipo_evento')

        # Validación para Concierto
        if tipo_evento == 'concierto':
            artista = cleaned_data.get('artista')
            duracion = cleaned_data.get('duracion')
            if not artista or not duracion:
                raise forms.ValidationError("Debe ingresar el artista y la duración para el concierto.")
        
        # Validación para Conferencia
        elif tipo_evento == 'conferencia':
            tema = cleaned_data.get('tema')
            orador = cleaned_data.get('orador')
            if not tema or not orador:
                raise forms.ValidationError("Debe ingresar el tema y el orador para la conferencia.")
        
        return cleaned_data
