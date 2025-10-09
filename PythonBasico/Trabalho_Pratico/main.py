import rich
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import os

console = Console()

arquivo_usuario = "usuarios.txt"
arquivo_produtos = "produtos.txt"

# Funções auxiliares

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r") as f:
        return [linha.strip().split(";") for linha in f.readlines() if linha.strip()]


def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        for item in dados:
            f.write(";".join(item) + "\n")

#Cadastro

import re
def validar_senha(senha):
    if len(senha) < 4:
        console.print("[red] A senha deve ter pelo menos 4 caracteres.[/red]")
        return False
    if not re.search("[A-Za-z]", senha):
        console.print("[red] A senha deve conter pelo menos uma letra.[/red]")
        return False
    if not re.search("[0-9]", senha):
        console.print("[red] A senha deve conter pelo menos um número.[/red]")
        return False
    return True

def cadastrar_usuario():
    console.print("\n[bold green]---Cadastro de Usuário---[/bold green]")
    nome = Prompt.ask("Nome de usuário")
    while True:
        senha = Prompt.ask("Senha", password = True)
        if validar_senha(senha):
            break
    usuarios = carregar_dados(arquivo_usuario)
    for user in usuarios:
        if user[0] == nome:
            console.print("[red]Usuário já existe![/red]")
            return
    usuarios.append([nome,senha])
    salvar_dados(arquivo_usuario, usuarios)
    console.print("[green]Usuário cadastrado com sucesso![/green]")

def login():
    console.print("\n[bold cyan]--- Login ---[/bold cyan]")
    nome = Prompt.ask("Usuário")
    senha = Prompt.ask("Senha", password=True)

    usuarios = carregar_dados(arquivo_usuario)
    for user in usuarios:
        if user[0] == nome and user[1] == senha:
            console.print(f"[green]Login bem-sucedido! Bem-vindo(a), {nome}![/green]")
            menu_usuario(nome)
            return
    console.print("[red]Usuário ou senha incorretos![/red]")


def atualizar_cadastro(usuario_logado):
    usuarios = carregar_dados(arquivo_usuario.txt)

    for user in usuarios:
        if user[0] == usuario_logado:
            console.print("\n[bold yellow]--- Atualizar Cadastro ---[/bold yellow]")
            nova_senha = Prompt.ask("Nova senha", password=True)
            user[1] = nova_senha
            salvar_dados(arquivo_usuario, usuarios)
            console.print("[green]Senha atualizada com sucesso![/green]")
            return
        
def excluir_usuario(usuarios, arquivo_csv):
    console.print("[bold red]Exclusão de Usuário[/bold red]\nPor favor, insira o nome do usuário a ser excluído.")
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")

# CRUD de Produtos/Serviços

def cadastrar_produto():
    console.print("\n[bold green]--- Cadastro de Produto/Serviço ---[/bold green]")
    nome = Prompt.ask("Nome do produto/serviço")
    preco = Prompt.ask("Preço (ex: 10.50)")
    quantidade = Prompt.ask("Quantidade")

    produtos = carregar_dados(arquivo_usuario)
    produtos.append([nome, preco, quantidade])
    salvar_dados(arquivo_produtos, produtos)
    console.print("[green]Produto/Serviço cadastrado com sucesso![/green]")

def listar_produtos():
    console.print("\n[bold cyan]--- Lista de Produtos/Serviços ---[/bold cyan]")
    produtos = carregar_dados(arquivo_produtos)
    if not produtos:
        console.print("[yellow]Nenhum produto/serviço cadastrado.[/yellow]")
        return

    tabela = Table(title="Produtos/Serviços Cadastrados")
    tabela.add_column("Nome", style="bold")
    tabela.add_column("Preço")
    tabela.add_column("Quantidade")

    for p in produtos:
        tabela.add_row(p[0], p[1], p[2])

    console.print(tabela)

def atualizar_produto():
    listar_produtos()
    nome = Prompt.ask("\nDigite o nome do produto/serviço que deseja atualizar")
    produtos = carregar_dados(arquivo_produtos)

    for p in produtos:
        if p[0] == nome:
            novo_preco = Prompt.ask("Novo preço")
            nova_qtd = Prompt.ask("Nova quantidade")
            p[1], p[2] = novo_preco, nova_qtd
            salvar_dados(arquivo_produtos, produtos)
            console.print("[green]Produto/Serviço atualizado com sucesso![/green]")
            return

    console.print("[red]Produto/Serviço não encontrado.[/red]")

def remover_produto():
    console.print("\n[bold red] --- Remover Produto/Serviço ---[/bold red]")
    nome = Prompt.ask("\nDigite o nome do produto/serviço que deseja remover")
    produtos = carregar_dados(arquivo_produtos)

    novos = [p for p in produtos if p[0].lower() != nome.lower()]
    if len(novos) == len(produtos):
        console.print("[red]Produto/Serviço não encontrado.[/red]")
        return

    salvar_dados(arquivo_produtos, novos)
    console.print("[green]Produto/Serviço removido com sucesso![/green]")

# Menu

def menu_usuario(usuario_logado):
    while True:
        console.print(f"\n[bold cyan]--- Menu do Usuário ({usuario_logado}) ---[/bold cyan]")
        console.print("[1] Atualizar cadastro")
        console.print("[2] Cadastrar produto/serviço")
        console.print("[3] Listar produtos/serviços")
        console.print("[4] Atualizar produto/serviço")
        console.print("[5] Remover produto/serviço")
        console.print("[6] Sair")

        opc = Prompt.ask("Escolha uma opção")

        if opc == "1":
            atualizar_cadastro(usuario_logado)
        elif opc == "2":
            cadastrar_produto()
        elif opc == "3":
            listar_produtos()
        elif opc == "4":
            atualizar_produto()
        elif opc == "5":
            remover_produto()
        elif opc == "6":
            console.print("[yellow]Saindo...[/yellow]")
            break
        else:
            console.print("[red]Opção inválida![/red]")


def menu_principal():
    while True:
        console.print("\n[bold blue]=== Sistema de Usuários e Produtos ===[/bold blue]")
        console.print("[1] Login")
        console.print("[2] Cadastrar novo usuário")
        console.print("[3] Sair")

        opc = Prompt.ask("Escolha uma opção")

        if opc == "1":
            login()
        elif opc == "2":
            cadastrar_usuario()
        elif opc == "3":
            console.print("[yellow]Encerrando o sistema...[/yellow]")
            break
        else:
            console.print("[red]Opção inválida![/red]")

#Armazenamento de dados

def salvar_dados(arquivo, dados):
    with open(arquivo, "a") as f:
        for item in dados:
            f.write(";".join(item)+"\n")

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r") as f:
        return [linha.strip().split(";") for linha in f.readlines() if linha.strip()]

# Execução
if __name__ == "__main__":
    menu_principal()