from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Plan(models.Model):
    tipo_plan = models.CharField(max_length=20, unique=True)
    precio_mensual = models.DecimalField(max_digits=8, decimal_places=0)
    descripcion = models.TextField(blank=True)   
    
    def __str__(self):
        return f"{self.tipo_plan}"

class Socio(models.Model):
    nombre = models.CharField(max_length=20,)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    dni = models.IntegerField(unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="socios",null=True, blank=True)
    fecha_ingreso = models.DateTimeField(default = timezone.now)
    cuota_vencimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
        
    def __str__(self):
        return f"{self.nombre}, {self.apellido} - DNI: {self.dni} - Cuota "
    
    def estado_cuota(self):
        if self.cuota_vencimiento >= timezone.now().date():
            return f"Al día"
        else:
            return f"Vencida"
    
    def dias_vencimiento(self) -> int | None:
        if not self.cuota_vencimiento:
            return None
        return (self.cuota_vencimiento - timezone.now().date()).days
    
    def save(self, *args, **kwargs):
        base = self.fecha_ingreso
        if isinstance(base, datetime):
            base = base.date()
        self.cuota_vencimiento = base + timedelta(days=365)
        super().save(*args, **kwargs)  
    
DIAS_SEMANA = [
    (1, "Lunes"),
    (2, "Martes"),
    (3, "Miércoles"),
    (4, "Jueves"),
    (5, "Viernes"),
    (6, "Sábado"),
]
   
class ClaseGrupal(models.Model):
    nombre_clase = models.CharField(max_length=80)
    dia_semana = models.IntegerField(choices = DIAS_SEMANA)
    hora = models.TimeField()
    cupo = models.PositiveIntegerField(default=30)
    class Meta:
        ordering = ["nombre_clase", "dia_semana", "hora"]
    

    def __str__(self):
        return f"{self.nombre_clase} – {self.get_dia_semana_display()} {self.hora:%H:%M}"
    