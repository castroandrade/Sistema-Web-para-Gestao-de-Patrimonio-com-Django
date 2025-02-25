from django.urls import path
from .views import lista_fornecedores, criar_fornecedor, editar_fornecedor, excluir_fornecedor

app_name = "fornecedores"

urlpatterns = [
    path("", lista_fornecedores, name="lista_fornecedores"),
    path("novo/", criar_fornecedor, name="criar_fornecedor"),
    path("editar/<int:fornecedor_id>/", editar_fornecedor, name="editar_fornecedor"),
    path("excluir/<int:fornecedor_id>/", excluir_fornecedor, name="excluir_fornecedor"),
]
