function emailValido(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function listarUsuarios() {
    window.location.href = "/usuarios/listar/";
}

async function cadastrarUsuario() {
    const nome = prompt("Nome:");

    if (nome === null) return;
    if (!nome) return alert("Nome obrigatório");

    const email = prompt("Email:");

    if (email === null) return;
    if (!email) return alert("Email obrigatório");
    if (!emailValido(email)) return alert("Email inválido");

    const senha = prompt("Senha:");
    if (senha === null) return;
    if (!senha) return alert("Senha obrigatória");

    try {
        const response = await fetch("/usuarios/add/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({ nome, email, senha }),
        });

        const data = await response.json();

        if (!response.ok) {
            if (data.error === "Senha fraca") {
                alert(
                    "Senha fraca:\n" +
                    data.regras.join("\n")
                );
            } else {
                alert(data.error || "Erro ao cadastrar usuário");
            }
        } else {
            alert(data.success);
        }
    } catch (err) {
        alert("Erro de conexão");
        console.error(err);
    }
}

async function excluirUsuario() {
    const email = prompt("Informe o email do usuário a ser excluído:");

    if (email === null) return;
    if (!email) return;

    if (!emailValido(email)) {
        alert("Email inválido");
        return;
    }

    if (!confirm("Tem certeza que deseja excluir este usuário?")) return;

    try {
        const response = await fetch("/usuarios/excluir/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({ email }),
        });

        const data = await response.json();

        if (!response.ok) {
            return alert(data.error || "Erro ao excluir");
        }

        alert(data.success);

        if (data.logout) {
            window.location.href = "/login/";
            return 2;
        }


    } catch (err) {
        alert("Erro de conexão");
    }
}

async function alterarSenha({ email }) {

    let btn = true;

    if (!email) {
        email = prompt("Email do usuário:");
        if (email === null) return;
    } else {
        btn = confirm("Deseja alterar a senha do seu usuário?")
    }

    if (btn === null) {
        return;
    }

    if (!btn) {
        return;
    }
    
    if (!email || !emailValido(email)) {
        return alert("Email inválido");
    }

    const novaSenha = prompt("Nova senha:");

    if (novaSenha === null) return;

    if (!novaSenha) return alert("Senha obrigatória");

    try {
        const response = await fetch("/usuarios/alterarsenha/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({
                email: email,
                senha: novaSenha
            }),
        });

        const data = await response.json();

        if (!response.ok) {
            if (data.error === "Senha fraca") {
                alert(
                    "Senha fraca:\n" +
                    data.regras.join("\n")
                );
            } else {
                alert(data.error || "Erro ao cadastrar usuário");
            }
        } else {
            alert(data.success);
        }
    } catch (err) {
        alert("Erro de conexão");
    }
}

async function menuUsuarios({opcao = false, email = false, ext = false}) {
    

    if (!opcao) {
        opcao = prompt(
        "Escolha uma opção:\n" +
        "1 = Listar usuários\n" +
        "2 = Cadastrar novo usuário\n" +
        "3 = Excluir usuário\n" +
        "4 = Alterar senha"
        );
    }

    if (!opcao) return;

    let a = 0;

    switch (opcao.trim()) {
        case "1":
            a = await listarUsuarios();
            break;
        case "2":
            a = await cadastrarUsuario();
            break;
        case "3":
            a = await excluirUsuario();
            break;
        case "4":
            a = await alterarSenha({ email });
            break;
        default:
            a = await alert("Opção inválida");
    }

    if (opcao != 1 && ext == false && a != 2) {
        menuUsuarios({});
    }
}
