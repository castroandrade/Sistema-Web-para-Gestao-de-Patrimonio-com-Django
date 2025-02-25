from django.shortcuts import render, get_object_or_404, redirect
from .models import Departamento
from .forms import DepartamentoForm
from django.contrib import messages

def lista_departamentos(request):
    """ Lista todos os departamentos """
    departamentos = Departamento.objects.all()
    return render(request, "departamentos/lista.html", {"departamentos": departamentos})

def criar_departamento(request):
    """ Cadastra um novo departamento """
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Departamento cadastrado com sucesso!")
            return redirect("departamentos:lista_departamentos")
    else:
        form = DepartamentoForm()

    return render(request, "departamentos/form.html", {"form": form, "titulo": "Adicionar Departamento"})

def editar_departamento(request, departamento_id):
    """ Edita um departamento existente """
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, "Departamento atualizado com sucesso!")
            return redirect("departamentos:lista_departamentos")
    else:
        form = DepartamentoForm(instance=departamento)

    return render(request, "departamentos/form.html", {"form": form, "titulo": "Editar Departamento"})

def excluir_departamento(request, departamento_id):
    """ Exclui um departamento """
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == "POST":
        departamento.delete()
        messages.success(request, "Departamento excluído com sucesso!")
        return redirect("departamentos:lista_departamentos")

    return render(request, "departamentos/confirmar_exclusao.html", {"departamento": departamento})
