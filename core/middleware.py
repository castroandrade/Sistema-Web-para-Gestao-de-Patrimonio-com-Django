from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    """Middleware para garantir que o usuário esteja autenticado em todas as páginas"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in ["/usuarios/login/", "/usuarios/registro/"]:
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
