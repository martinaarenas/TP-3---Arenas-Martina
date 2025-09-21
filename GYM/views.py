from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Socio, Plan, ClaseGrupal, DIAS_SEMANA
from .forms import SocioForm, ClasesForm, PlanesForm


def inicio(request):
    return render(request, "GYM/inicio.html")

def socios_list(request):
    socios = Socio.objects.all()
    query = request.GET.get("query", "").strip()
    if query !="":
       socios = socios.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(dni__icontains=query)
        )
    else:
       socios = socios.all()
    contexto = {"socios": socios,"query": query}
    return render(request, "GYM/socios_list.html", contexto)

def planes_list(request):
    if request.method == "POST":
        plan = Plan.objects.get(pk=request.POST["plan_id"])
        plan.precio_mensual = request.POST["precio_mensual"]
        plan.save(update_fields=["precio_mensual"])

    planes = Plan.objects.all().order_by("tipo_plan")
    return render(request, "GYM/planes_list.html", {"planes": planes})

def clases_list(request):
    clases = ClaseGrupal.objects.all()
    dia = request.GET.get("dia", "").strip()
    if dia !="":
       clases = clases.filter(dia_semana__icontains = dia)
    else:
        clases = clases.all()
    contexto = {"clases": clases, "dia": dia, "DIAS_SEMANA": DIAS_SEMANA,}
    return render(request, "GYM/clases_list.html", contexto)

def crear_socios(request):
    if request.method == "POST": 
        formulario = SocioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("socios_list")
    else:
        formulario = SocioForm()
    return render(request, "GYM/socio_form.html", {"form": formulario})

def registrar_clase(request):
    if request.method == "POST": 
        formulario = ClasesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("clases_list")
    else:
        formulario = ClasesForm()
    return render(request, "GYM/clases_form.html", {"form": formulario})

def registrar_plan(request):
    if request.method == "POST": 
        formulario = PlanesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("planes_list")
    else:
        formulario = PlanesForm()
    return render(request, "GYM/planes_form.html", {"form": formulario})
            