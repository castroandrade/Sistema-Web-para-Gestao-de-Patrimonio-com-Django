from django.shortcuts import render, get_object_or_404, redirect
from .models import Bem
from .forms import BemForm
from django.contrib import messages

def lista_bens(request):
    """ Lista todos os bens cadastrados """
    bens = Bem.objects.all()
    return render(request, "patrimonio/lista.html", {"bens": bens})

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
