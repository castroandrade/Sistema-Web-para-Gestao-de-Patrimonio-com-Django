from django.urls import path
from .views import lista_bens, criar_bem, editar_bem, excluir_bem

app_name = "patrimonio"

urlpatterns = [
    path("", lista_bens, name="lista_bens"),
    path("novo/", criar_bem, name="criar_bem"),
    path("editar/<int:bem_id>/", editar_bem, name="editar_bem"),
    path("excluir/<int:bem_id>/", excluir_bem, name="excluir_bem"),
]
