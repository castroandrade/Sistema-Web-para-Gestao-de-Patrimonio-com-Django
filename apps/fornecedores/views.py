from django.shortcuts import render, get_object_or_404, redirect
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib import messages

def lista_fornecedores(request):
    """ Lista todos os fornecedores """
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedores/lista.html", {"fornecedores": fornecedores})

def criar_fornecedor(request):
    """ Cadastra um novo fornecedor """
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor cadastrado com sucesso!")
            return redirect("fornecedores:lista_fornecedores")
    else:
        form = FornecedorForm()

    return render(request, "fornecedores/form.html", {"form": form, "titulo": "Adicionar Fornecedor"})

def editar_fornecedor(request, fornecedor_id):
    """ Edita um fornecedor existente """
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor atualizado com sucesso!")
            return redirect("fornecedores:lista_fornecedores")
    else:
        form = FornecedorForm(instance=fornecedor)

    return render(request, "fornecedores/form.html", {"form": form, "titulo": "Editar Fornecedor"})

def excluir_fornecedor(request, fornecedor_id):
    """ Exclui um fornecedor """
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == "POST":
        fornecedor.delete()
        messages.success(request, "Fornecedor excluído com sucesso!")
        return redirect("fornecedores:lista_fornecedores")

    return render(request, "fornecedores/confirmar_exclusao.html", {"fornecedor": fornecedor})
