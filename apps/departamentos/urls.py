from django.urls import path
from .views import lista_departamentos, criar_departamento, editar_departamento, excluir_departamento

app_name = "departamentos"

urlpatterns = [
    path("", lista_departamentos, name="lista_departamentos"),
    path("novo/", criar_departamento, name="criar_departamento"),
    path("editar/<int:departamento_id>/", editar_departamento, name="editar_departamento"),
    path("excluir/<int:departamento_id>/", excluir_departamento, name="excluir_departamento"),
]
