from django.views import View
from django.shortcuts import render, redirect

class UsuariosView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'pages/usuarios/usuarios.html', {
            "scripts": ["js/usuarios/usuarios.js"],
        })