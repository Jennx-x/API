from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Concierto, Conferencia
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import EventoForm

# Vista principal que carga la página con el CRUD
def index(request):
    return render(request, 'project/index.html')

# Vista para crear un evento (Concierto o Conferencia)
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            tipo_evento = form.cleaned_data['tipo_evento']
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            lugar = form.cleaned_data['lugar']

            # Crear el evento según el tipo seleccionado
            if tipo_evento == 'concierto':
                artista = form.cleaned_data['artista']
                duracion = form.cleaned_data['duracion']
                Concierto.objects.create(
                    nombre=nombre, fecha=fecha, lugar=lugar,
                    artista=artista, duracion=duracion
                )
            elif tipo_evento == 'conferencia':
                tema = form.cleaned_data['tema']
                orador = form.cleaned_data['orador']
                Conferencia.objects.create(
                    nombre=nombre, fecha=fecha, lugar=lugar,
                    tema=tema, orador=orador
                )
            return redirect('lista_eventos')  # Redirigir después de guardar el evento
    else:
        form = EventoForm()

    return render(request, 'index.html', {'form': form})

# Vista para listar eventos (Conciertos y Conferencias)
def listar_evento(request):
    # Obtener los conciertos y conferencias
    conciertos = Concierto.objects.all()
    conferencias = Conferencia.objects.all()

    eventos = []

    # Agregar conciertos a la lista de eventos
    for concierto in conciertos:
        evento = {
            'tipo_evento': 'concierto',  # Se agrega el tipo de evento explícitamente
            'nombre': concierto.nombre,
            'fecha': concierto.fecha,
            'lugar': concierto.lugar,
            'artista': concierto.artista,
            'duracion': concierto.duracion,
        }
        eventos.append(evento)

    # Agregar conferencias a la lista de eventos
    for conferencia in conferencias:
        evento = {
            'tipo_evento': 'conferencia',  # Se agrega el tipo de evento explícitamente
            'nombre': conferencia.nombre,
            'fecha': conferencia.fecha,
            'lugar': conferencia.lugar,
            'tema': conferencia.tema,
            'orador': conferencia.orador,
        }
        eventos.append(evento)

    return JsonResponse(eventos, safe=False)

# Vista para actualizar un evento
@csrf_exempt
def actualizar_evento(request, evento_id):
    if request.method == 'PUT':
        # Intentar obtener el evento como un Concierto o Conferencia
        try:
            evento = Concierto.objects.get(id=evento_id)
            evento_tipo = 'concierto'
        except Concierto.DoesNotExist:
            evento = get_object_or_404(Conferencia, id=evento_id)
            evento_tipo = 'conferencia'

        data = json.loads(request.body)

        # Actualizar campos comunes
        evento.nombre = data.get('nombre', evento.nombre)
        evento.fecha = data.get('fecha', evento.fecha)
        evento.lugar = data.get('lugar', evento.lugar)

        # Actualizar campos específicos de concierto o conferencia
        if evento_tipo == 'concierto':
            evento.artista = data.get('artista', evento.artista)
            evento.duracion = data.get('duracion', evento.duracion)
        else:  # Si es conferencia
            evento.tema = data.get('tema', evento.tema)
            evento.orador = data.get('orador', evento.orador)

        evento.save()

        return JsonResponse({'message': 'Evento actualizado con éxito', 'evento': evento.id})


# Vista para eliminar un evento
@csrf_exempt
def eliminar_evento(request, evento_id):
    if request.method == 'DELETE':
        # Intentar obtener el evento como un Concierto o Conferencia
        try:
            evento = Concierto.objects.get(id=evento_id)
        except Concierto.DoesNotExist:
            evento = get_object_or_404(Conferencia, id=evento_id)

        evento.delete()

        return JsonResponse({'message': 'Evento eliminado con éxito'})
