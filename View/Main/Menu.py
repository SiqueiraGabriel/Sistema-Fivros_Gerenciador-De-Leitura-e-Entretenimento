from tkinter import *


def semAcao():
    print()

def criarMenu(app):
    barraMenu = Menu(app)

#Criação do SubMenu de Usuários
    menuUsuario = Menu(barraMenu, tearoff=0)
    menuUsuario.add_command(label="Adicionar Novo Usuário", command=semAcao)
    menuUsuario.add_command(label="Ver Perfil", command=semAcao)
    menuUsuario.add_command(label="Realizar Login", command=semAcao)
    menuUsuario.add_separator()
    menuUsuario.add_command(label="Sair", command=app.quit)

#Criação do subMenu de Livros
    menuLivros = Menu(barraMenu, tearoff=0)
    menuLivros.add_command(label="Adicionar Novo Livro", command=semAcao)
    menuLivros.add_command(label="Adicionar Escritor", command=semAcao)
    menuLivros.add_command(label="Visualizar Livros Cadastrados")
    menuLivros.add_separator()
    menuLivros.add_command(label="Gerar Relatório em PDF", command=semAcao)

#Criação de subMenu de Filmes
    menuFilmes = Menu(barraMenu, tearoff=0)
    menuFilmes.add_command(label="Adicionar Novo Filme", command=semAcao)
    menuFilmes.add_command(label="Adicionar Diretor", command=semAcao)
    menuFilmes.add_command(label="Visualizar Filmes Cadastrados", command=semAcao)
    menuFilmes.add_separator()
    menuFilmes.add_command(label="Gerar Relatório em PDF", command=semAcao)

#Criação de subMenu de Séries
    menuSeries = Menu(barraMenu, tearoff=0)
    menuSeries.add_command(label="Adicionar Novo Filme", command=semAcao)
    menuSeries.add_command(label="Adicionar Diretor", command=semAcao)
    menuSeries.add_command(label="Visualizar Séries Cadastradas", command=semAcao)
    menuSeries.add_separator()
    menuSeries.add_command(label="Gerar Relatório em PDF", command=semAcao)

#Criação do Menu de Ajuda
    menuSobre = Menu(barraMenu, tearoff=0)
    menuSobre.add_command(label="Informações do Aplicativo", command=semAcao)
    menuSobre.add_command(label="Instruções para Utilização", command=semAcao)



# Junção dos menus
    barraMenu.add_cascade(label="Usuário", menu=menuUsuario)
    barraMenu.add_cascade(label="Livros", menu=menuLivros)
    barraMenu.add_cascade(label="Filmes", menu=menuFilmes)
    barraMenu.add_cascade(label="Séries", menu=menuSeries)
    barraMenu.add_cascade(label="Sobre", menu=menuSobre)

#Sincronização do menu com a página
    app.config(menu=barraMenu)

