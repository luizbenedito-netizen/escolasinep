from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import make_password
from app.utils.fns import senha_forte
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from app.models import CadUsuarios, CadMunicipios


@require_POST
def addUsuario(request):
    
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")


    campos_obrigatorios = {
        "nome": nome,
        "email": email,
        "senha": senha,
    }

    campos_vazios = [campo for campo, valor in campos_obrigatorios.items() if not valor]

    if campos_vazios:
        return JsonResponse(
            {
                "error": "Campos obrigatórios não informados",
                "campos": campos_vazios
            },
            status=400
        )
        
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse(
            {"error": "Email inválido"},
            status=400
        )
        
    if not senha_forte(senha):
        return JsonResponse(
            {
                "error": "Senha fraca",
                "regras": [
                    "mínimo 12 caracteres",
                    "pelo menos 3 números",
                    "pelo menos 1 caractere especial"
                ]
            },
            status=400
        )


    if CadUsuarios.objects.filter(email=email).exists():
        return JsonResponse(
            {"error": "Já existe um usuário com este email"},
            status=409
        )

    if CadUsuarios.objects.filter(nome=nome).exists():
        return JsonResponse(
            {"error": "Já existe um usuário com este nome"},
            status=409
        )


    cpf = "11111111111"
    datanascimento = "2000-01-01"
    idmunicipio = "3144102"

    try:
        municipio = CadMunicipios.objects.get(idmunicipio=idmunicipio)
    except CadMunicipios.DoesNotExist:
        return JsonResponse(
            {"error": "Município não encontrado"},
            status=400
        )

    
    senha_hash = make_password(senha, hasher="bcrypt_sha256")

    usuario = CadUsuarios.objects.create(
        nome=nome,
        cpf=cpf,
        datanascimento=datanascimento,
        email=email,
        idmunicipio=municipio,
        senha=senha_hash,
        ativo=True
    )


    return JsonResponse(
        {
            "success": "Usuário cadastrado com sucesso!",
            "id": usuario.idusuario
        },
        status=201
    )
    
@require_POST
def excluir_usuario(request):
    email = request.POST.get("email")

    if not email:
        return JsonResponse(
            {"error": "Email obrigatório"},
            status=400
        )

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse(
            {"error": "Email inválido"},
            status=400
        )

    try:
        usuario = CadUsuarios.objects.get(email=email)
    except CadUsuarios.DoesNotExist:
        return JsonResponse(
            {"error": "Usuário não encontrado"},
            status=404
        )
        
    if usuario.pk == 1:
        return JsonResponse(
            {"error": "Este usuário não pode ser excluído"},
            status=403
        )
        
    session_user_id = request.session.get("user_id")
    is_self_delete = session_user_id == usuario.idusuario

    usuario.delete()

    if is_self_delete:
        request.session.flush()
        return JsonResponse(
            {
                "success": "Usuário excluído definitivamente",
                "logout": True
            },
            status=200
        )

    return JsonResponse(
        {"success": "Usuário excluído definitivamente"},
        status=200
    )
    
@require_POST
def alterar_senha(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    if not email or not senha:
        return JsonResponse(
            {"error": "Email e senha são obrigatórios"},
            status=400
        )
        
    if not senha_forte(senha):
        return JsonResponse(
            {
                "error": "Senha fraca",
                "regras": [
                    "mínimo 12 caracteres",
                    "pelo menos 3 números",
                    "pelo menos 1 caractere especial"
                ]
            },
            status=400
        )

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"error": "Email inválido"}, status=400)

    try:
        usuario = CadUsuarios.objects.get(email=email, ativo=True)
    except CadUsuarios.DoesNotExist:
        return JsonResponse({"error": "Usuário não encontrado"}, status=404)

    usuario.senha = make_password(senha, hasher="bcrypt_sha256")
    usuario.tokensenha = None  # opcional
    usuario.save(update_fields=["senha", "tokensenha"])

    return JsonResponse(
        {"success": "Senha alterada com sucesso"},
        status=200
    )
    
def listar_usuarios(request):
    
    usuarios = CadUsuarios.objects.values("nome", "email")

    return JsonResponse(
        list(usuarios),
        safe=False,
        status=200
    )
