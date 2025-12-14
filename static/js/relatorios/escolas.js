// ---------------------------------------------
// Vars
// ---------------------------------------------

let formBtn;

// ---------------------------------------------
// Helpers
// ---------------------------------------------

function toggleButton () {
    const collapses = document.querySelectorAll("[data-collapse-toggle]");

    collapses.forEach(toggle => {
        const icon = toggle.querySelector(".rotate-icon");
        const targetId = toggle.getAttribute("data-collapse-toggle");
        const target = document.getElementById(targetId);

        if (!target || !icon) return;

        // Usando eventos do Flowbite
        target.addEventListener("show.flowbite", () => {
        icon.classList.add("rotate-180");
        });

        target.addEventListener("hide.flowbite", () => {
        icon.classList.remove("rotate-180");
        });
    });
}

const req = (el) => el.dataset.reqValue;

const btnSubmit = (status) => {
    formBtn.disabled = !status;
}

async function inicializarSelect(args) {

    const { 
        api, 
        cacheName, 
        select,
        dataEach,
        dataCacheName = () => "all",
        callBack,
        isTrigger = false
    } = args;

    async function fetchAndCache(cache) {
        const [resp] = await Promise.all([
            fetch(api()),
            new Promise(resolve => setTimeout(resolve, isTrigger ? 1500 : 0))
        ]);
        const data = await resp.json();
        cache[dataCacheName()] = data;
        localStorage.setItem(cacheName, JSON.stringify(cache));
        return cache;
    }

    async function loadCache() {

        btnSubmit(false);
        select.innerHTML = "<option>Carregando...</option>";

        let cache = localStorage.getItem(cacheName);
        cache = cache ? JSON.parse(cache) : {};
        cache = !cache[dataCacheName()] ? await fetchAndCache(cache) : cache;
        return cache[dataCacheName()];
    }

    function popularSelect(data) {

        select.innerHTML = "<option value='0'>Todos</option>";

        const reqValue = select.getAttribute("attr-req-value");

        for (const item of data) {
            const opt = document.createElement("option");

            opt.value = item[dataEach.value];
            opt.textContent = item[dataEach.textContent];

            if (String(req(select)) === String(item[dataEach.value])) {
                opt.selected = true;
            }

            select.appendChild(opt);
        }

        btnSubmit(true);
    }

    const data = await loadCache();
    popularSelect(data);

    if (typeof callBack === "function") {
        callBack({...args, callBack: null});
    }
}

function excluirButtons () {

    const modalEl = document.getElementById("popup-modal");

    const modal = new Modal(modalEl, {
        closable: true,
        backdrop: 'dynamic',
    });

    let excludeId = null;

    // Abrir modal
    document.querySelectorAll(".excluir").forEach(btn => {
        btn.addEventListener("click", () => {
        excludeId = btn.dataset.exclude;
        });
    });

    
    // Confirmar exclusão
    document.getElementById("confirm-exclude")
    .addEventListener("click", () => {

        if (!excludeId) return;

        fetch(`/relatorios/escolas/excluir/${excludeId}`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(),
        },
        })
        .then(() => {
            window.location.reload();
        })
        .catch(() => {
            window.location.reload();
        });

        // CSRF Django
        function getCSRFToken() {
            return document.querySelector("[name=csrfmiddlewaretoken]").value;
        }
    });
}

// ---------------------------------------------
// DOM Ready
// ---------------------------------------------
document.addEventListener("DOMContentLoaded", () => {

    excluirButtons();
    toggleButton();

    formBtn = document.getElementById("form-button");

    const estadoSelect = document.getElementById("estado");
    const cidadeSelect = document.getElementById("cidade");
    const localSelect = document.getElementById("local");
    const categoriaSelect = document.getElementById("categoria");

    // Estados
    inicializarSelect({
        api: () => "/relatorios/escolas/estados/",
        cacheName: "estados-cache",
        select: estadoSelect,
        dataEach: { value: "iddistrito", textContent: "nome" }
    });

    // Cidades (dependem de estado)
    inicializarSelect({
        api: () => `/relatorios/escolas/cidades/?estado=${req(estadoSelect)}`,
        cacheName: "cidades-cache",
        dataCacheName: () => req(estadoSelect),
        select: cidadeSelect,
        dataEach: { value: "idmunicipio", textContent: "nome" },
        callBack: (args) => {

            // Estado → recarrega cidades
            estadoSelect.addEventListener("change", function handler() {
                this.dataset.reqValue = this.value;
                inicializarSelect({...args, isTrigger: true});
            });

            // Cidade → só atualiza dataset
            cidadeSelect.addEventListener("change", function() {
                this.dataset.reqValue = this.value;
            });
        }
    });

    // Locais
    inicializarSelect({
        api: () => "/relatorios/escolas/locais/",
        cacheName: "locais-cache",
        select: localSelect,
        dataEach: { value: "cod", textContent: "descricao" }
    });

    // Categorias
    inicializarSelect({
        api: () => "/relatorios/escolas/categorias/",
        cacheName: "categorias-cache",
        select: categoriaSelect,
        dataEach: { value: "cod", textContent: "descricao" }
    });

});