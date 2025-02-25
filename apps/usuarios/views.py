from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('usuarios:login')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("dashboard")  # Redireciona para a dashboard
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")

    return render(request, "usuarios/login.html")

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect("usuarios:login")  # Redireciona para a tela de login após cadastro
        else:
            messages.error(request, "Ocorreu um erro ao tentar cadastrar. Verifique os dados.")
    else:
        form = UserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})


#TODO: meu perfil

@login_required
def perfil_usuario(request):
    return render(request, "usuarios/perfil.html", {"user": request.user})