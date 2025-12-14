from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect

from app.models import CadEscolas, CadMunicipios, CadDistritos, CadTipos

def getEstados(request):
    
    estados = list(
        CadDistritos.objects
        .values("iddistrito", "nome")
        .order_by("nome")
    )
    
    return JsonResponse(estados, safe=False, json_dumps_params={'ensure_ascii': False})
    

def getCidades(request):
    
    estado = request.GET.get("estado")

    if not estado:
        return JsonResponse({"error": "Parâmetro 'estado' é obrigatório."}, status=400)

    cidades = list(
        CadMunicipios.objects.filter(iddistrito=estado)
        .values("idmunicipio", "nome")
        .order_by("nome")
    )

    return JsonResponse(cidades, safe=False, json_dumps_params={'ensure_ascii': False})

def getLocais(request):
    
    locais = list(
        CadTipos.objects
        .filter(campo="Local")
        .values("cod", "descricao")
        .order_by("descricao")
    )
    
    return JsonResponse(locais, safe=False, json_dumps_params={'ensure_ascii': False})


def getCategorias(request):
    
    categorias = list(
        CadTipos.objects
        .filter(campo="Categoria")
        .values("cod", "descricao")
        .order_by("descricao")
    )
    
    return JsonResponse(categorias, safe=False, json_dumps_params={'ensure_ascii': False})

def delEscola(request, idescola):
    
    updated = CadEscolas.objects.filter(
        idescola=idescola,
        ativo=True
    ).update(ativo=False)

    if updated:
        msg = "Escola desativada com sucesso."
        # messages.success(request, msg)
        return JsonResponse({"msg": msg, "status": True}, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        msg =  "Escola não encontrada ou já estava desativada."
        # messages.warning(request, msg)
        return JsonResponse({"msg": msg, "status": False}, safe=False, json_dumps_params={'ensure_ascii': False})

    
    
    