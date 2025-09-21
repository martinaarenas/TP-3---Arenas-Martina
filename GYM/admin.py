from django.contrib import admin
from .models import Socio, Plan, ClaseGrupal

@admin.register(ClaseGrupal)
class ClasesAdmin(admin.ModelAdmin):
    list_display = ("nombre_clase", "dia_semana", "hora", "cupo",)
    search_fields = ("nombre_clase",)
    list_filter = ("dia_semana",)
    
@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "plan", "cuota_vencimiento","estado_cuota",)
    search_fields = ("dni",)
    list_filter = ("activo",)
    readonly_fields = ("cuota_vencimiento",)
    list_per_page = 10
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("tipo_plan", "precio_mensual", "descripcion",)
    