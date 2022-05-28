import os
from os import *
from Modulos.Usuario import *
from Modulos.Documento import *

caminho = os.path.dirname(__file__)

def adicionarConteudo():
    exec(open(caminho + "\\NovoContato.py").read())

def semAcao():
    print()

def criarMenu(app, idUsuario):
    app.config(menu="")
    barraMenu = Menu(app)

#Criação do SubMenu de Usuários
    menuUsuario = Menu(barraMenu, tearoff=0)
    menuUsuario.add_command(label="Adicionar Novo Usuário", command=lambda:Usuario().createViewCadastro(app))
    menuUsuario.add_command(label="Ver Perfil", command=lambda:Usuario().createViewPerfil(app, idUsuario))
    menuUsuario.add_command(label="Realizar Login", command=lambda:Usuario().createViewLogar(app))
    menuUsuario.add_separator()
    menuUsuario.add_command(label="Sair", command=app.quit)

#Criação do subMenu de Conteudo
    menuConteudo = Menu(barraMenu, tearoff=0)
    menuConteudo.add_command(label="Adicionar Conteúdo", command=lambda:Documento().createViewDocumento(app=app, idUsuario=idUsuario))
    menuConteudo.add_command(label="Alterar Conteúdo", command=lambda:Documento().createViewAlteraDoc(app=app, idUsuario=idUsuario))
    menuConteudo.add_command(label="Excluir Conteúdo", command=lambda:Documento().createViewDelete(app=app, idUsuario=idUsuario))

    #menuConteudo.add_separator()
    #menuConteudo.add_command(label="Gerar Relatório em PDF", command=semAcao)

#Criação do Menu de Ajuda
    menuSobre = Menu(barraMenu, tearoff=0)
    menuSobre.add_command(label="Informações do Aplicativo", command=semAcao)
    menuSobre.add_command(label="Instruções para Utilização", command=semAcao)

# Junção dos menus
    barraMenu.add_cascade(label="Usuário", menu=menuUsuario)
    barraMenu.add_cascade(label="Conteúdo", menu=menuConteudo)
    barraMenu.add_cascade(label="Sobre", menu=menuSobre)

#Sincronização do menu com a página
    app.config(menu=barraMenu)

def criarMenuInicial(app):
    barraMenu = Menu(app)

    # Criação do SubMenu de Usuários
    menuUsuario = Menu(barraMenu, tearoff=0)
    menuUsuario.add_command(label="Adicionar Novo Usuário", command=lambda: Usuario().createViewCadastro(app))
    menuUsuario.add_command(label="Ver Perfil", command=semAcao)
    menuUsuario.add_command(label="Realizar Login", command=lambda: Usuario().createViewLogar(app))
    menuUsuario.add_separator()
    menuUsuario.add_command(label="Sair", command=app.quit)

    # Criação do Menu de Ajuda
    menuSobre = Menu(barraMenu, tearoff=0)
    menuSobre.add_command(label="Informações do Aplicativo", command=semAcao)
    menuSobre.add_command(label="Instruções para Utilização", command=semAcao)

    # Junção dos menus
    barraMenu.add_cascade(label="Usuário", menu=menuUsuario)
    barraMenu.add_cascade(label="Sobre", menu=menuSobre)

    # Sincronização do menu com a página
    app.config(menu=barraMenu)