from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(blank=True, null=True)
    creditos = models.IntegerField(default=3)
    semestre = models.IntegerField(null=False, blank=False)
    docente = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False, blank=False)
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA, null=False, blank=False)
    hora_inicio = models.TimeField(null=False, blank=False)
    hora_fin = models.TimeField(null=False, blank=False)
    aula = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.materia} - {self.get_dia_semana_display()} {self.hora_inicio} a {self.hora_fin}"

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
