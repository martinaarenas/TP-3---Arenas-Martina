from django import forms
from .models import Socio, ClaseGrupal, Plan, DIAS_SEMANA

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ["nombre", "apellido", "email", "dni", "plan", "fecha_ingreso", "activo"]
        widgets = {"fecha_ingreso": forms.DateInput(attrs = {"type": "date"})}
        error_messages = {"dni": {"unique": "DNI ya existente",}}
        
class ClasesForm(forms.ModelForm):
    class Meta:
        model = ClaseGrupal
        fields = ["nombre_clase", "dia_semana", "hora", "cupo"]
        ordering = ["nombre_clase", "dia_semana", "hora"]
        widgets = {"dia_semana": forms.Select(choices = DIAS_SEMANA), "hora": forms.TimeInput(attrs={"type": "time"}),}
        
class PlanesForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ["tipo_plan", "precio_mensual", "descripcion"]
        labels = {"precio_mensual": "Precio mensual ($)"}

        
       
    
 