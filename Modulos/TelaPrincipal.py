from Modulos.ClasseCategoria import *
import os.path
from tkinter import *
from tkinter import ttk

import Modulos.Menu
from Modulos.DimensoesTela.DimensaoTelaPrincipal import *


class TelaPrincipal:

    def __init__(self, app):
        print()

    def semAcao(self):
        print()

    def criar(self, app, idUsuario):
        self.idUsuario = idUsuario
        framePrincipal = Frame(app)
        Modulos.Menu.criarMenu(app, idUsuario=idUsuario)
        framePrincipal.place(x=10, y=30, width=1340, height=670)
        self.criacaoAbas(framePrincipal)




    def criacaoAbas(self, aba):

        #Criação do Frames principais
        self.fr_Principal = Frame(aba, borderwidth=1, relief='ridge')


        #Criação dos Frames Secundários
        self.fr_Conteudo = Frame(aba, borderwidth=1, relief='ridge')
        self.fr_Menu = Frame(aba, borderwidth=1, relief='ridge')
        self.fr_Titulo = Frame(self.fr_Conteudo)

        #Adição do Menu Lateral
        self.btnAbrirMenu = Button(self.fr_Conteudo, text="|||", background="#8C1018", foreground="#fff", command=self.abrirMenu)
        self.addMenuLateral(self.fr_Menu)

        #Criação do Topo da Página
        self.criarTopoPagina()

        #Configuração das dimensões
        DimeElemetCriacaoAbas(self.fr_Conteudo, self.fr_Menu, self.fr_VisualizarCategoria, self.lblCategoria, self.optMenuCategoria, self.btnSelecionarCategoria, self.fr_Titulo, self.titulo)

        # Criação da Aba Dentro aba
        self.fr_ApresentaAba = Frame(self.fr_Conteudo)
        self.abaSituacao = ttk.Notebook(self.fr_ApresentaAba, padding=2)

        #Adicionar os valores de Situação
        self.addAppCategoriaSituacao(self.fr_Conteudo)


        #Retorno dos frames de Conteúdo e Menu
        self.fr_ApresentaAba.place(x=25, y=150, width=1000, height=150)
        self.abaSituacao.place(x=0, y=0, width=1000, height=150)


    def criarTopoPagina(self):
        listaCategoria = Categoria().returnAllCategoria()
        self.varCategoria = StringVar()
        self.titulo = Label(self.fr_Titulo, text="MEUS CONTEÚDOS CADASTRADOS", anchor="center", font=("Arial", 15))
        self.fr_VisualizarCategoria = Frame(self.fr_Titulo)
        self.lblCategoria = Label(self.fr_VisualizarCategoria, text="Visualizar Categoria", background="#635959",
                                  font=("Arial", 10), foreground="#f6f6f6")
        self.optMenuCategoria = OptionMenu(self.fr_VisualizarCategoria, self.varCategoria, *listaCategoria)
        self.btnSelecionarCategoria = Button(self.fr_VisualizarCategoria, text="Selecionar",
                                             command=lambda: self.addAppCategoriaSituacao(self.fr_Conteudo))


    def addTreView(self, fr_Responsavel, colunaAutor, status, idCategoria):

        if(status == "Todos"):
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero', 'status'), show="headings")
            tv.column('genero', minwidth=50, width=150)
            tv.column('status', minwidth=25, width=80)
            tv.heading('status', text="STATUS")
        else:
            tv = ttk.Treeview(fr_Responsavel, columns=('id','nome','autor','genero'), show="headings")
            tv.column('genero', minwidth=150, width=230)


        tv.column('id', minwidth=25, width=50)
        tv.column('nome', minwidth=150, width=550)
        tv.column('autor', minwidth=50, width=160)
        tv.heading('id', text="ID")
        tv.heading('nome',text="NOME")
        tv.heading('autor', text=colunaAutor.upper())
        tv.heading('genero', text="GÊNERO")


        tv.pack(pady=10)

        self.insertValuesOfCategoria(tv, idCategoria, status)


    def addAppCategoriaSituacao(self, fr_Conteudo):



        #Valor após escolher a Categoria
        if self.varCategoria.get() != []:
            idCategoria = Categoria().returnIdCategoria(self.varCategoria.get())
            autor = Categoria().returnAutorCategoria(idCategoria)


        #Valor Padrão da Categoria
        if idCategoria == None:
            idCategoria = 17
            autor = Categoria().returnAutorCategoria(idCategoria)


        #Frames da Aba Situacao
        fr_Todos = Frame(fr_Conteudo)
        fr_Recomendado = Frame(fr_Conteudo)
        fr_Iniciado = Frame(fr_Conteudo)
        fr_Finalizado = Frame(fr_Conteudo)
        fr_FantasmaMemoria = Frame(fr_Conteudo)

        #limpar Aba Principal



        #Aba Todos
        self.abaSituacao.add(fr_Todos, text="Todos")
        self.addTreView(fr_Todos, autor, "Todos", idCategoria)

        #Aba Recomendado
        self.abaSituacao.add(fr_Recomendado, text="Recomendado")
        #self.addTreView(fr_Recomendado, autor, "Recomendado", "Livro")

        #aba Iniciado
        self.abaSituacao.add(fr_Iniciado, text="Iniciado")
        #self.addTreView(fr_Iniciado, autor, "Iniciado", "Livro")

        #aba Finalizado
        self.abaSituacao.add(fr_Finalizado, text="Finalizado")
        #self.addTreView(fr_Finalizado, autor, "Finalizado", "Livro")

        #aba FantasmaMemoria
        self.abaSituacao.add(fr_FantasmaMemoria, text="Fantasma na Memória")
        #self.addTreView(fr_FantasmaMemoria, autor, "Fantasma na Memória", "Livro")


    def insertValuesOfCategoria(self, abaCategoria, idCategoria, status):
        #Recuperar todos os valores da Categoria


        abaCategoria.insert("", 'end', values=('1', 'A Volta ao Mundo em 80 dias', 'Julio Verne', 'Aventura', 'Finalizado'))







    def addMenuLateral(self, fr_Menu):
        #Adição dos elementos
        self.btnFecharMenu = Button(fr_Menu, text="|||", background="#8C1018", foreground="#fff", command=self.fecharMenu)
        btnAdicionar = Button(fr_Menu, text="Adicionar", command=self.semAcao)
        btnAlterar = Button(fr_Menu, text="Alterar", command=self.semAcao)
        btnExcluir = Button(fr_Menu, text="Excluir ", command=self.semAcao)
        btnVisualizar = Button(fr_Menu, text="Visualização Completa", command=self.semAcao)
        btnRelatorio = Button(fr_Menu, text="Gerar Relatório em PDF", command=self.semAcao)
        lblMenuTitulo = Label(fr_Menu, text="Fivros", anchor="center", font=("Arial", 16, "bold"))

        #Configuração das dimensões
        DimeElementMenuLateral(self.btnFecharMenu, lblMenuTitulo, btnAdicionar, btnAlterar, btnExcluir, btnVisualizar, btnRelatorio)


    def abrirMenu(self):
        DimeElementAbrirMenu(self.fr_Menu, self.fr_Conteudo, self.btnAbrirMenu, self.fr_Titulo, self.titulo, self.fr_VisualizarCategoria, self.abaSituacao)


    def fecharMenu(self):
        DimeElementFecharMenu(self.fr_Menu, self.fr_Principal, self.fr_Conteudo, self.abaSituacao, self.btnAbrirMenu, self.fr_Titulo, self.fr_VisualizarCategoria)


