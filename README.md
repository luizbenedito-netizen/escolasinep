# 📚 Escolas INEP

> **Acompanhe as escolas do Brasil todo sem dificuldades!**

## 🎓 Sobre o Projeto

**Escolas INEP** é uma plataforma acadêmica desenvolvida com o objetivo de facilitar o acompanhamento, a consulta e o gerenciamento de informações sobre todas as escolas do Brasil.

O sistema foi projetado para lidar com um grande volume de registros, permitindo **filtragens avançadas**, **paginação eficiente** e **renderização otimizada**, tornando a análise dos dados muito mais rápida e organizada do que os métodos tradicionais.

Este projeto foi desenvolvido como parte do curso de **Ciência da Computação**.

---

## 🎯 Objetivos

- Centralizar informações sobre escolas brasileiras
- Facilitar a busca e filtragem de dados educacionais
- Oferecer relatórios claros e organizados
- Demonstrar a aplicação prática de conceitos de desenvolvimento web e banco de dados

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django**
- **PostgreSQL**

### Frontend
- **Tailwind CSS**
- **Flowbite**

### Técnicas e Funcionalidades
- Paginação de dados
- Sistema de autenticação
- Recuperação de senha via link seguro
- Criptografia de senhas
- Filtros avançados de informações
- Cache de dados para renderização otimizada

---

## ⚙️ Funcionalidades do Sistema

- Sistema de Autenticação de Usuários
- Recuperação de Senha
- Relatórios de Escolas
- Filtro Avançado de Escolas
- Paginação de Registros
- Cadastro, Edição, Exclusão e Alteração de Senha de Usuários

---

## 🌐 Páginas e Rotas Principais

- `Home/`
- `Relatorios/Escolas/`
- `Login/`
- `Login/esquecisenha/`
- `Login/resetarsenha/`
- `Usuarios/`
  - `Usuarios/listar/`
  - `Usuarios/add/`
  - `Usuarios/excluir/`
  - `Usuarios/alterar/`
- `Escolas/`
  - `Escolas/cidades/`
  - `Escolas/estados/`
  - `Escolas/locais/`
  - `Escolas/categorias/`

---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

---

### 2️⃣ Instalar as dependências do Python

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Instalar as dependências do Frontend

```bash
npm install
```

---

### 4️⃣ Configurar o Banco de Dados (PostgreSQL)

- Crie um banco de dados no PostgreSQL.
- Importe o arquivo de banco de dados fornecido, localizado em `bd/bd.sql` (contendo a estrutura e os dados).
- A importação pode ser feita utilizando o **PgAdmin** através da opção *Restore*.

---

### 5️⃣ Configurar variáveis de ambiente

- Renomear o arquivo `.env.development` para `.env`
- Preencher as informações de conexão com o PostgreSQL

#### 🔐 Gerar a chave `RECOVERY_KEY`

A chave deve seguir o padrão exigido pelo **Fernet** (32 bytes codificados em base64).

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

### 6️⃣ Executar o projeto

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000
```

---

### 7️⃣ Compilação e acompanhamento do CSS

Para desenvolvimento, é necessário rodar o **Makefile** para que o Tailwind acompanhe as alterações de estilo:

```bash
make -f MakeFile
```

---

## 📌 Status do Projeto

🎓 **Projeto acadêmico finalizado**, com margem para melhorias e novas funcionalidades.

---

## 🔗 Links

- Repositório GitHub: https://github.com/luizbenedito-netizen/escolasinep
- Demo: https://luizcodifica.com/login/ (usuário: luiz, senha: 3fCe£Bj=R0AF;FB£0"+7KnjZZ70I60'fe)

---

## 👤 Autor

**Luiz Otávio de P. B.**  
Curso: Ciência da Computação  
Instituição: IFSULDEMINAS – Campus Muzambinho  
GitHub: https://github.com/luizbenedito-netizen

---

## 📄 Licença

Este projeto é destinado exclusivamente para **uso acadêmico**.

