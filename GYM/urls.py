from django.urls import path
from .views import inicio, socios_list, planes_list, clases_list, crear_socios, registrar_clase, registrar_plan 


urlpatterns = [
               path("", inicio, name ="inicio"),
               path("socios/", socios_list, name ="socios_list"),
               path("planes/", planes_list, name ="planes_list"),
               path("clases/", clases_list, name ="clases_list"),
               path("crear_socios", crear_socios, name ="crear_socios"),
               path("registrar_clase", registrar_clase, name="registrar_clase"),
               path("registrar_plan", registrar_plan, name="registrar_plan"),]

