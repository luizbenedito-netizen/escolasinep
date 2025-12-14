from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages

from app.models import CadUsuarios
from app.utils.fns import senha_forte
from django.contrib.auth.hashers import make_password, check_password

class LoginView(View):
    
    @staticmethod
    def logout(request):
        request.session.flush()
        return redirect("/login")
    
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/login/login.html')
    
    def post(self, request, *args, **kwargs):
        
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        lembrar = request.POST.get('lembrar')
        
        if not senha_forte(senha):
                messages.error(request, "Usuário ou senha inválidos")
        else:
            try:
                user = CadUsuarios.objects.get(nome=usuario)
                
                if check_password(senha, user.senha):
                
                    request.session['user_id'] = user.idusuario
                    request.session['username'] = user.nome
                    request.session['email'] = user.email
                    
                    if lembrar:
                        request.session.set_expiry(0)
                    
                    # Permissões
                    # request.session['permissoes'] = ...
                    
                    return redirect('home')
                else:
                    messages.error(request, "Usuário ou senha inválidos")
            except CadUsuarios.DoesNotExist:
                messages.error(request, "Usuário ou senha inválidos")
            
        return render(request, 'pages/login/login.html')
