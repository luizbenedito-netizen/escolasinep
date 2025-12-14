from django.views import View
from django.shortcuts import render, redirect
from app.utils.filters import extract_filters, apply_filters, paginate, build_querystring

from app.models import CadDistritos, EscolaView

class EscolasView(View):
    
    def get(self, request, *args, **kwargs):

        FILTER_CONFIG = {
            "page": {
                "default": "1",
            },
            "estado": {
                "default": "0",
                "field": "idestado",
                "apply_if": lambda v: v != "0",
            },
            "cidade": {
                "default": "0",
                "field": "idcidade",
                "apply_if": lambda v: v != "0",
            },
            "local": {
                "default": "0",
                "field": "idlocal",
                "apply_if": lambda v: v != "0",
            },
            "categoria": {
                "default": "0",
                "field": "idcategoria",
                "apply_if": lambda v: v != "0",
            },
            "nome_op": {
                "default": "0",
            },
            "nome": {
                "default": "",
                "field": "nome",
                "apply_if": lambda v: v != "",
                "operator_param": "nome_op",
            },
            "escola_op": {
                "default": "0",
            },
            "escola": {
                "default": "",
                "field": "idescola",
                "apply_if": lambda v: v != "",
                "operator_param": "escola_op",
            },
        }

        filters = extract_filters(request, FILTER_CONFIG)

        qs = None
        page_obj = None
        querystring = None

        if request.GET:
            qs = apply_filters(
                EscolaView.objects.all(),
                filters,
                FILTER_CONFIG
            ).filter(ativo=True).order_by('nome')
            page_obj = paginate(qs, filters["page"])
            querystring = build_querystring(filters, FILTER_CONFIG, exclude=["page"])

        return render(request, 'pages/relatorios/escolas.html', {
            "page_obj": page_obj,
            "filters": filters,
            "querystring": querystring,
            "scripts": [
                "js/relatorios/escolas.js",
            ],
        })