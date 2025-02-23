from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('usuarios:login')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo, {user.firstnameUsuario}! Você está logado com sucesso.")
                return redirect('')  # Redireciona após o login bem-sucedido
            else:
                messages.error(request, "Email ou senha incorretos.")
                return render(request, 'usuarios/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    messages.error(request, "Email ou senha incorretos.")
    return render(request, "usuarios/login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/register.html", {"form": form})

#TODO: meu perfil