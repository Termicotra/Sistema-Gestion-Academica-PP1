from django.contrib import admin
from .models import Materia, Horario

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos', 'semestre', 'docente')
    ordering = ['semestre']
    search_fields = ['nombre']
    list_filter = ['nombre']

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia_semana', 'hora_inicio', 'hora_fin', 'aula')
    ordering = ['dia_semana']
