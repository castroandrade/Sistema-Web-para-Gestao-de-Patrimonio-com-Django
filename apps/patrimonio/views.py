from django.shortcuts import render, get_object_or_404, redirect
from .models import Bem, Categoria
from .forms import BemForm
from django.contrib import messages
from django.db.models import Q
from apps.departamentos.models import Departamento

def lista_bens(request):
    """Listagem de bens patrimoniais com filtros e ordenação"""
    bens = Bem.objects.all()
    categorias = Categoria.objects.all()
    departamentos = Departamento.objects.all()

    # 🔹 Filtro por Categoria
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        bens = bens.filter(categoria_id=categoria_id)

    # 🔹 Filtro por Status
    status = request.GET.get("status")
    if status:
        bens = bens.filter(status=status)

    # 🔹 Filtro por Departamento
    departamento_id = request.GET.get("departamento")
    if departamento_id:
        bens = bens.filter(departamento_id=departamento_id)

    # 🔹 Busca por nome do bem
    busca = request.GET.get("q")
    if busca:
        bens = bens.filter(Q(nome__icontains=busca) | Q(identificador_rfid__icontains=busca))

    # 🔹 Ordenação dinâmica
    ordenacao = request.GET.get("ordenacao", "nome")  # Padrão: ordenar por nome
    bens = bens.order_by(ordenacao)

    context = {
        "bens": bens,
        "categorias": categorias,
        "departamentos": departamentos,
        "ordenacao": ordenacao
    }
    return render(request, "patrimonio/lista.html", context)

def criar_bem(request):
    """ Cria um novo bem patrimonial """
    if request.method == "POST":
        form = BemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bem cadastrado com sucesso!")
            return redirect("patrimonio:lista_bens")
    else:
        form = BemForm()

    return render(request, "patrimonio/form.html", {"form": form, "titulo": "Adicionar Bem"})

def editar_bem(request, bem_id):
    """ Edita um bem patrimonial existente """
    bem = get_object_or_404(Bem, id=bem_id)
    if request.method == "POST":
        form = BemForm(request.POST, instance=bem)
        if form.is_valid():
            form.save()
            messages.success(request, "Bem atualizado com sucesso!")
            return redirect("patrimonio:lista_bens")
    else:
        form = BemForm(instance=bem)

    return render(request, "patrimonio/form.html", {"form": form, "titulo": "Editar Bem"})

def excluir_bem(request, bem_id):
    """ Exclui um bem patrimonial """
    bem = get_object_or_404(Bem, id=bem_id)
    if request.method == "POST":
        bem.delete()
        messages.success(request, "Bem excluído com sucesso!")
        return redirect("patrimonio:lista_bens")

    return render(request, "patrimonio/confirmar_exclusao.html", {"bem": bem})
